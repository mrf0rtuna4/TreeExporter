from tree_exporter.models import TreeNode


def generate_svg(
    tree: TreeNode,
    output: str = "structure.svg",
) -> None:

    """
    Render repository tree into SVG.

    TODO:
    - calculate layout
    - add collapsible nodes
    - add colors by file type
    - add links
    """

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg">
    <text x="20" y="30">
        {tree.name}
    </text>
</svg>
"""

    with open(
        output,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(svg)