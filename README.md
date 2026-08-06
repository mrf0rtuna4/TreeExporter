<div align="center">

# 🌳 TreeExporter

**Automatically generate beautiful repository structure diagrams from your project.**

_No more manually maintaining folder trees in your README._

<p>
    <img src="https://img.shields.io/pypi/v/TreeExporter?style=for-the-badge&logo=pypi" />
    <img src="https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge&logo=python" />
    <img src="https://img.shields.io/github/actions/workflow/status/mrf0rtuna4/TreeExporter/generate-structure.yml?style=for-the-badge" />
</p>

</div>

---

## Why?

Keeping a repository structure up to date is surprisingly annoying.

Every time files or folders change, developers have to manually edit the tree inside the documentation:

```text
src
├── api
├── models
├── utils
└── ...
```

Which quickly becomes outdated.

**TreeExporter** scans your project and generates a clean, automatically updated visualization instead.

It can be:

- updated automatically with GitHub Actions
- used as a Python library
- used as a CLI tool
- exported to SVG or plain text

---

## 🖼 Demo

### SVG

![Repository Structure](./docs/structure.svg)

```md
![Repository Structure](./docs/structure.svg)
```

### Text

Look at `./docs/structure.txt`

---

## 🚀 Features

- Repository scanning
- SVG export
- Plain text export
- Configurable excluded directories
- GitHub Actions support
- Python library API
- Fast recursive traversal

More formats are planned.

---

## Installation

Using **uv** (recommended):

```bash
uv tool install TreeExporter
```

or install into the current environment:

```bash
uv add TreeExporter
```

Using **pip**:

```bash
pip install TreeExporter
```

---

## 💻 CLI

Generate a repository structure:

```bash
tree-exporter
```

Generate SVG into `docs/tree.svg`:

```bash
tree-exporter \
    --format svg \
    --output docs/tree
```

Exclude additional directories:

```bash
tree-exporter \
    --exclude ".venv,dist,build"
```

Replace the default exclusion list:

```bash
tree-exporter \
    --exclude-overwrite \
    --exclude ".git"
```

---

## GitHub Actions

Automatically regenerate your repository structure on a schedule or after every push.

```yaml
- uses: mrf0rtuna4/TreeExporter@v0.1.0
  with:
    format: svg
    output: docs/structure
```

Perfect for keeping documentation synchronized with your project.

---

## Library

TreeExporter can also be used directly from Python.

```python
from tree_exporter.config import ScanConfig
from tree_exporter.scanner import scan_repository

tree = scan_repository(
    ".",
    ScanConfig(),
)
```

---

## Roadmap

- ✅ Text export
- ✅ SVG export
- ✅ GitHub Action
- 🔄 Themes
- 🚧 Mermaid export
- 🚧 JSON export
- 🚧 PNG export
- 🚧 Custom icons
- 🚧 Ignore file support
