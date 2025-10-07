# md2pdf

A command-line tool for converting Markdown files to PDF.

## Installation

### Option 1: Install to ~/bin (recommended for shell usage)

```bash
git clone https://github.com/kristofer/md2pdf.git
cd md2pdf
./install.sh
```

This will:
- Install the md2pdf package and its dependencies
- Create an executable script in `~/bin/md2pdf`
- Provide instructions for adding `~/bin` to your PATH

### Option 2: Install with pip

```bash
git clone https://github.com/kristofer/md2pdf.git
cd md2pdf
pip install -e .
```

Or install directly from the repository:

```bash
pip install git+https://github.com/kristofer/md2pdf.git
```

## Usage

Convert a Markdown file to PDF:

```bash
md2pdf input.md
```

Specify an output file:

```bash
md2pdf input.md -o output.pdf
```

Get help:

```bash
md2pdf --help
```

## Requirements

- Python 3.6 or higher
- Dependencies (automatically installed):
  - markdown
  - weasyprint

## Examples

```bash
# Convert README.md to README.pdf
md2pdf README.md

# Convert with custom output name
md2pdf documentation.md -o docs.pdf

# Using from Python module
python -m md2pdf input.md
```

## Features

- Simple command-line interface
- Converts Markdown to well-formatted PDF
- Supports standard Markdown syntax
- Code highlighting
- Tables and blockquotes
- Custom CSS styling

## License

MIT License - see LICENSE file for details
