from dataclasses import dataclass

from tree_exporter.models import TreeNode


@dataclass(slots=True)
class LayoutNode:
    node: TreeNode
    depth: int
    y: int


def build_layout(root: TreeNode) -> list[LayoutNode]:
    result: list[LayoutNode] = []

    def visit(node: TreeNode, depth: int) -> None:
        result.append(
            LayoutNode(
                node=node,
                depth=depth,
                y=len(result),
            )
        )

        for child in sorted(
            node.children,
            key=lambda n: (
                not n.is_directory,
                n.name.lower(),
            ),
        ):
            visit(child, depth + 1)

    visit(root, 0)

    return result
