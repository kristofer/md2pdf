"""Markdown to PDF conversion logic."""

import markdown
from weasyprint import HTML
from pathlib import Path


def get_bundled_css_path(css_name):
    """
    Get the path to a bundled CSS file.
    
    Args:
        css_name: Name of the CSS file (e.g., 'pandoc.css', 'footer.css')
    
    Returns:
        Path to the bundled CSS file, or None if not found
    """
    package_dir = Path(__file__).parent
    css_path = package_dir / "css" / css_name
    return str(css_path) if css_path.exists() else None


def convert_md_to_pdf(input_file, output_file, css_files=None):
    """
    Convert a Markdown file to PDF.
    
    Args:
        input_file: Path to the input Markdown file
        output_file: Path to the output PDF file
        css_files: Optional list of CSS file paths to include for styling
    """
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
    
    # Load custom CSS if provided
    custom_css = ""
    if css_files:
        for css_file in css_files:
            css_path = Path(css_file)
            if css_path.exists():
                with open(css_path, 'r', encoding='utf-8') as f:
                    custom_css += f.read() + "\n"
    
    # Add basic CSS styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 3px;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }}
            blockquote {{
                border-left: 4px solid #ccc;
                margin-left: 0;
                padding-left: 20px;
                color: #666;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f4f4f4;
            }}
            {custom_css}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Convert HTML to PDF
    HTML(string=styled_html).write_pdf(output_file)
