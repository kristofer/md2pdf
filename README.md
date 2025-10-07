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

Use custom CSS styling:

```bash
md2pdf input.md -c custom.css
```

Use multiple CSS files:

```bash
md2pdf input.md -c style1.css -c style2.css
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

# Using custom CSS for styling
md2pdf report.md -c mystyle.css

# Using multiple CSS files
md2pdf report.md -c base.css -c theme.css
```

## Features

- Simple command-line interface
- Converts Markdown to well-formatted PDF
- Supports standard Markdown syntax
- Code highlighting
- Tables and blockquotes
- Custom CSS styling

## Custom CSS Styling

md2pdf allows you to customize the appearance of your PDFs using CSS files. The tool comes with bundled CSS files and also supports your own custom CSS.

### Bundled CSS Files

The package includes two pre-configured CSS files in the `md2pdf/css/` directory:

- **pandoc.css**: Provides Pandoc-style formatting with Helvetica fonts and responsive sizing
- **footer.css**: Adds a custom footer to PDF pages with copyright information

To use bundled CSS files, reference them from the package installation:

```bash
# Get the path to bundled CSS
python -c "from md2pdf.converter import get_bundled_css_path; print(get_bundled_css_path('pandoc.css'))"

# Use bundled CSS in conversion
md2pdf document.md -c $(python -c "from md2pdf.converter import get_bundled_css_path; print(get_bundled_css_path('pandoc.css'))")
```

Or create a simple helper script:

```bash
#!/bin/bash
# md2pdf-styled.sh - Convert with bundled CSS

PANDOC_CSS=$(python -c "from md2pdf.converter import get_bundled_css_path; print(get_bundled_css_path('pandoc.css'))")
FOOTER_CSS=$(python -c "from md2pdf.converter import get_bundled_css_path; print(get_bundled_css_path('footer.css'))")

md2pdf "$1" -c "$PANDOC_CSS" -c "$FOOTER_CSS"
```

Usage: `./md2pdf-styled.sh document.md`

### Using Your Own CSS

You can create your own CSS files and apply them to your PDFs:

```bash
# Create a custom CSS file
cat > my-style.css << 'EOF'
body {
    font-family: Georgia, serif;
    font-size: 14px;
}

h1 {
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
}
EOF

# Use it in conversion
md2pdf document.md -c my-style.css
```

### Combining Multiple CSS Files

You can combine multiple CSS files for more complex styling:

```bash
md2pdf document.md -c base-style.css -c custom-footer.css -c code-theme.css
```

### CSS Tips

- Custom CSS is applied after the default styling, so it will override default styles
- Use `@page` rules in CSS to customize page margins, headers, and footers
- WeasyPrint supports most CSS properties for print media
- You can inspect the bundled CSS files for examples: `md2pdf/css/pandoc.css` and `md2pdf/css/footer.css`

## License

MIT License - see LICENSE file for details
