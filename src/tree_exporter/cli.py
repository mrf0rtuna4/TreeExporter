import typer

from tree_exporter.config import ScanConfig
from tree_exporter.renderer import (
    generate_svg,
    generate_txt,
)
from tree_exporter.scanner import scan_repository


app = typer.Typer(
    name="tree-exporter",
    help="Generate visual repository structures.",
)


@app.command()
def generate(
    path: str = typer.Option(
        ".",
        help="Repository path",
    ),

    output: str = typer.Option(
        "structure.txt",
        help="Output file",
    ),

    format: str = typer.Option(
        "txt",
        help="Output format: txt/svg",
    ),

    exclude: list[str] = typer.Option(
        [],
        help="Excluded directories",
    ),
):

    config = ScanConfig(
        exclude=set(exclude),
    )

    tree = scan_repository(
        path,
        config,
    )

    match format:

        case "txt":
            generate_txt(
                tree,
                output,
            )

        case "svg":
            generate_svg(
                tree,
                output,
            )

        case _:
            raise typer.BadParameter(
                f"Unsupported format: {format}"
            )

    typer.echo(
        f"Generated {output}"
    )


if __name__ == "__main__":
    app()