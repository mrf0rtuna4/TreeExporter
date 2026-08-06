from pathlib import Path

from tree_exporter.models import TreeNode


def generate_txt(
    tree: TreeNode,
    output: str = "structure.txt",
) -> None:
    """
    Generate tree representation.

    TODO:
    - support unicode tree characters
    - support max depth
    - support file metadata
    """

    lines: list[str] = [tree.name]

    _render_children(
        tree,
        prefix="",
        lines=lines,
    )

    Path(output).write_text(
        "\n".join(lines),
        encoding="utf-8",
    )


def _render_children(
    node: TreeNode,
    prefix: str,
    lines: list[str],
) -> None:

    children = sorted(
        node.children,
        key=lambda item: (
            not item.is_directory,
            item.name.lower(),
        ),
    )

    for index, child in enumerate(children):
        is_last = index == len(children) - 1

        if is_last:
            branch = "\\-- "
            next_prefix = prefix + "    "
        else:
            branch = "+-- "
            next_prefix = prefix + "|   "

        lines.append(prefix + branch + child.name)

        if child.is_directory:
            _render_children(
                child,
                next_prefix,
                lines,
            )
