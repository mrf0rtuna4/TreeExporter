<div align="center">

# 🌳 TreeExporter

**Automatically generate beautiful repository structure diagrams from your project.**

*No more manually maintaining folder trees in your README.*

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

* updated automatically with GitHub Actions
* used as a Python library
* used as a CLI tool
* exported to SVG, JSON or plain text

---

## 🖼 Demo

### SVG

![Repository Structure](./docs/structure.svg)

```md
![Repository Structure](./docs/structure.svg)
```

### Text

Look at [`./docs/structure.txt`](./docs/structure.txt).

---

## 🚀 Features

* Repository scanning
* SVG export
* Plain text export
* JSON export
* Custom SVG icons for directories and files
* Built-in SVG themes
* Configurable excluded directories
* GitHub Actions support
* Python library API
* Fast recursive traversal

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

By default, this generates:

```text
structure.svg
```

### Output format

Generate SVG:

```bash
tree-exporter \
    --format svg \
    --output docs/tree
```

Generate plain text:

```bash
tree-exporter \
    --format txt \
    --output docs/tree
```

Generate structured JSON:

```bash
tree-exporter \
    --format json \
    --output docs/tree
```

The output extension is added automatically. JSON contains each node's `name`, `type`, and recursively ordered `children`.

### Themes

SVG output supports built-in themes:

```bash
tree-exporter \
    --format svg \
    --output docs/tree \
    --theme dark
```

### Custom icons

SVG labels use folder and file emojis by default. Replace either icon with any text or emoji:

```bash
tree-exporter \
    --directory-icon "🗂️" \
    --file-icon "📝"
```

Available themes:

```text
light
dark
github-light
github-dark
dracula
monokai
nord
solarized-light
solarized-dark
one-dark
```

See [Themes](/docs/themes.md) for previews.

### Excluding directories

Add directories to the default exclusion list:

```bash
tree-exporter \
    --exclude ".venv,dist,build"
```

You can also repeat the option:

```bash
tree-exporter \
    --exclude ".venv,dist" \
    --exclude "coverage,node_modules"
```

### Replacing default exclusions

Use `--exclude-overwrite` to replace the default exclusion list completely:

```bash
tree-exporter \
    --exclude-overwrite \
    --exclude ".git,.venv"
```

---

## GitHub Actions

TreeExporter can automatically generate and update your repository structure using GitHub Actions.

### Basic usage

The simplest setup is:

```yaml
name: Generate repository structure

on:
  workflow_dispatch:

  push:
    branches:
      - master

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest

    steps:
      - name: Generate repository structure
        uses: mrf0rtuna4/TreeExporter@v0.2.0
        with:
          format: svg
          output: docs/structure

      - name: Commit and push
        shell: bash
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

          git add -A

          if git diff --cached --quiet; then
            echo "Repository structure is up-to-date."
            exit 0
          fi

          git commit -m "Update repository structure"
          git push
```

This will generate `docs/structure.svg` and commit it when the repository structure changes.

### Action inputs

| Input               | Default                       | Description                                          |
| ------------------- | ----------------------------- | ---------------------------------------------------- |
| `path`              | `.`                           | Repository path to scan                              |
| `output`            | `structure`                   | Output path without extension                        |
| `format`            | `svg`                         | Export format: `svg`, `txt`, or `json`               |
| `theme`             | `light`                       | SVG theme                                            |
| `directory-icon`    | `📁`                          | Directory icon in SVG output                         |
| `file-icon`         | `📄`                          | File icon in SVG output                              |
| `exclude`           | `""`                          | Additional excluded directories, separated by commas |
| `exclude-overwrite` | `false`                       | Replace default exclusions instead of extending them |
| `commit`            | `false`                       | Commit generated files                               |
| `commit-message`    | `Update repository structure` | Commit message                                       |
| `branch`            | `""`                          | Target branch                                        |

### Using a theme

For example, generate a dark-themed structure:

```yaml
- name: Generate repository structure
  uses: mrf0rtuna4/TreeExporter@v0.2.0
  with:
    format: svg
    output: docs/structure
    theme: dark
```

Or use Dracula:

```yaml
- name: Generate repository structure
  uses: mrf0rtuna4/TreeExporter@v0.2.0
  with:
    format: svg
    output: docs/structure
    theme: dracula
```

### Excluding directories

Additional exclusions can be configured directly in the Action:

```yaml
- name: Generate repository structure
  uses: mrf0rtuna4/TreeExporter@v0.2.0
  with:
    format: svg
    output: docs/structure
    exclude: ".venv,dist,build,node_modules"
```

To completely replace the default exclusions:

```yaml
- name: Generate repository structure
  uses: mrf0rtuna4/TreeExporter@v0.2.0
  with:
    format: svg
    output: docs/structure
    exclude-overwrite: "true"
    exclude: ".git,.venv"
```

### Complete example

A more complete workflow can look like this:

```yaml
name: Generate repository map

on:
  workflow_dispatch:

  push:
    branches:
      - master

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v7
        with:
          fetch-depth: 0

      - name: Generate repository structure
        uses: mrf0rtuna4/TreeExporter@v0.2.0
        with:
          format: svg
          output: docs/structure
          theme: dark
          exclude: ".venv,dist,build"

      - name: Commit and push
        shell: bash
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

          git add -A

          if git diff --cached --quiet; then
            echo "Repository structure is up-to-date."
            exit 0
          fi

          git commit -m "Update repository structure"
          git push
```

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

* ✅ Repository scanning
* ✅ Text export
* ✅ SVG export
* ✅ GitHub Action
* ✅ Built-in themes
* 🚧 Mermaid export
* ✅ JSON export
* 🚧 PNG export
* ✅ Custom icons
* 🚧 Ignore file support
* 🧠 Interactive HTML export with collapsible directories
* 🧠 Per-file language icons and syntax-aware colors
* 🧠 Git diff mode for structural changes between revisions
* 🧠 Project config file for reusable defaults

---

## License

See the [LICENSE](./LICENSE) file for details.
