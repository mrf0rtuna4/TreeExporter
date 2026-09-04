from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from tree_exporter.models import TreeNode


def tree_to_dict(tree: TreeNode) -> dict[str, Any]:
    return {
        "name": tree.name,
        "type": "directory" if tree.is_directory else "file",
        "children": [tree_to_dict(child) for child in _sorted_children(tree)]
    }


def generate_json(tree: TreeNode, output: str = "structure.json") -> None:
    Path(output).write_text(
        json.dumps(tree_to_dict(tree),
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )


def _sorted_children(tree: TreeNode) -> list[TreeNode]:
    return sorted(
        tree.children,
        key=lambda item: (not item.is_directory, item.name.lower()),
    )
