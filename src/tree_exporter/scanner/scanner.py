from pathlib import Path
from typing import Any

DEFAULT_IGNORE = {
    ".git",
    ".venv",
    "node_modules",
    "__pycache__",
}


def scan_repository(path: str) -> list[Any]:
    root = Path(path)

    result: list[Any] = []

    for item in sorted(root.rglob("*")):
        if any(ignored in item.parts for ignored in DEFAULT_IGNORE):
            continue

        result.append(str(item.relative_to(root)))

    return result
