from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_EXCLUDES = {
    ".git",
    ".venv",
    "node_modules",
    "__pycache__",
    ".idea",
    ".vscode",
    ".ruff_cache",
    "dist",
    "build",
}


@dataclass
class ScanConfig:
    """
    Scanner configuration.

    TODO:
    - support glob patterns
    - support regex filters
    - support .treeexporter.yml
    """

    include_only: list[str] = field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]

    exclude: set[str] = field(default_factory=lambda: DEFAULT_EXCLUDES.copy())

    respect_gitignore: bool = True


def load_ignore_file(path: str = ".gitignore") -> list[str]:
    file = Path(path)

    if not file.exists():
        return []

    return [
        line.strip()
        for line in file.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]
