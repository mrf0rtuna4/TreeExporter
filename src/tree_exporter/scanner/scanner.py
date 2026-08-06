from pathlib import Path

from tree_exporter.config import ScanConfig
from tree_exporter.models import TreeNode


def should_ignore(
    path: Path,
    config: ScanConfig,
) -> bool:

    return any(part in config.exclude for part in path.parts)


def scan_repository(
    root_path: str,
    config: ScanConfig | None = None,
) -> TreeNode:

    config = config or ScanConfig()

    root = Path(root_path).resolve()

    root_node = TreeNode(
        name=root.name,
        path=root,
        is_directory=True,
    )

    _scan_directory(
        root,
        root_node,
        config,
    )

    return root_node


def _scan_directory(
    directory: Path,
    parent: TreeNode,
    config: ScanConfig,
) -> None:

    for item in sorted(
        directory.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower())
    ):
        if should_ignore(item, config):
            continue

        node = TreeNode(
            name=item.name,
            path=item,
            is_directory=item.is_dir(),
        )

        parent.add_child(node)

        if item.is_dir():
            _scan_directory(
                item,
                node,
                config,
            )
