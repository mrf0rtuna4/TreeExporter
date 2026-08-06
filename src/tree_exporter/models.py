from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class TreeNode:
    """
    Represents a filesystem node.

    TODO:
    - add size information
    - add git metadata
    - add language detection
    """

    name: str
    path: Path
    is_directory: bool

    children: list["TreeNode"] = field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]

    def add_child(self, node: "TreeNode") -> None:
        self.children.append(node)
