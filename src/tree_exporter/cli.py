from __future__ import annotations

from pathlib import Path
from typing import Literal

import typer

from tree_exporter.config import DEFAULT_EXCLUDES, ScanConfig
from tree_exporter.renderer import generate_svg, generate_txt
from tree_exporter.scanner import scan_repository

app = typer.Typer(
    name="tree-exporter",
    help="Generate visual repository structures.",
)

INVALID_OUTPUT_CHARS = {"*", "?", "<", ">", ":", '"', "|", "\\"}


def validate_repository_path(value: str) -> str:
    repo_path = Path(value).expanduser()

    if not repo_path.exists():
        raise typer.BadParameter(f"Repository path does not exist: {value}")

    if not repo_path.is_dir():
        raise typer.BadParameter(f"Repository path is not a directory: {value}")

    return str(repo_path)


def validate_output_base(value: str) -> str:
    raw = value.strip()

    if not raw:
        raise typer.BadParameter("Output path cannot be empty.")

    if raw.startswith(("/", "\\")):
        raise typer.BadParameter("Output path must be relative, not absolute.")

    if any(char in raw for char in INVALID_OUTPUT_CHARS):
        raise typer.BadParameter(
            'Output path contains invalid characters: * ? < > : " | \\'
        )

    normalized = raw.replace("\\", "/")
    parts = [part for part in normalized.split("/") if part]

    if not parts:
        raise typer.BadParameter("Output path cannot be empty.")

    if any(part in {".", ".."} for part in parts):
        raise typer.BadParameter("Output path cannot contain '.' or '..' segments.")

    if Path(normalized).suffix:
        raise typer.BadParameter(
            "Do not include a file extension in output. "
            "Use output='structure' and format='svg' or format='txt'."
        )

    return normalized


def parse_excludes(values: list[str]) -> set[str]:
    return {
        part.strip() for value in values for part in value.split(",") if part.strip()
    }


def resolve_output_path(output_base: str, output_format: Literal["txt", "svg"]) -> str:
    extension = ".svg" if output_format == "svg" else ".txt"
    return f"{output_base}{extension}"


def build_excludes(
    additional_excludes: list[str],
    overwrite_defaults: bool,
) -> set[str]:
    extra = parse_excludes(additional_excludes)

    if overwrite_defaults:
        return extra

    return set(DEFAULT_EXCLUDES) | extra


@app.command()
def generate(
    path: str = typer.Option(
        ".",
        help="Repository path",
        callback=validate_repository_path,
    ),
    output: str = typer.Option(
        "structure",
        help="Output file path without extension",
        callback=validate_output_base,
    ),
    format: Literal["txt", "svg"] = typer.Option(
        "svg",
        help="Output format: txt/svg",
    ),
    exclude: list[str] = typer.Option(
        [],
        help="Excluded directories separated by comma. Can be repeated.",
    ),
    exclude_overwrite: str = typer.Option(
        "false",
        help="Replace default excludes",
    )
):
    overwrite = exclude_overwrite.lower() == "true"

    config = ScanConfig(
        exclude=build_excludes(
            additional_excludes=exclude,
            overwrite_defaults=overwrite,
        ),
    )

    tree = scan_repository(
        path,
        config,
    )

    output_path = resolve_output_path(
        output_base=output,
        output_format=format,
    )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    match format:
        case "txt":
            generate_txt(
                tree,
                output_path,
            )
        case "svg":
            generate_svg(
                tree,
                output_path,
            )

    typer.echo(f"Generated {output_path}")


if __name__ == "__main__":
    app()
