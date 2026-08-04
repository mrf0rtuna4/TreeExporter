from pathlib import Path
from typing import Any

DEFAULT_IGNORE_FILE = ".gitignore"


def load_ignore_file(path: str = DEFAULT_IGNORE_FILE) -> list[Any] | list[str]:
    file = Path(path)

    if not file.exists():
        return []

    return [
        line.strip()
        for line in file.read_text().splitlines()
        if line.strip()
    ]
