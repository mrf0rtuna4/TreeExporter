import typer

from tree_exporter.scanner import scan_repository

app = typer.Typer(
    name="tree_exporter", help="Generate visual maps of repository structure."
)


@app.command()
def generate(
    path: str = ".",
):

    result = scan_repository(path)

    for item in result:
        typer.echo(item)


if __name__ == "__main__":
    app()
