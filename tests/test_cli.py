from pathlib import Path

from pytest import MonkeyPatch
from typer.testing import CliRunner

from tree_exporter.cli import app, build_excludes, resolve_output_path

runner = CliRunner()

def test_cli_generates_json(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()
    (repository / "readme.md").write_text("hello")

    monkeypatch.chdir(tmp_path)

    result = runner.invoke(
        app,
        ["--path", str(repository), "--format", "json", "--output", "result/tree"],
    )

    assert result.exit_code == 0, result.output
    assert (tmp_path / "result" / "tree.json").exists()

def test_cli_helpers_parse_excludes_and_extensions() -> None:
    assert build_excludes(["dist, coverage", "node_modules"], True) == {
        "dist",
        "coverage",
        "node_modules",
    }
    assert resolve_output_path("docs/tree", "json") == "docs/tree.json"
