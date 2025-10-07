"""CLI interface for md2pdf."""

import argparse
import os
import sys
from pathlib import Path
from md2pdf.converter import convert_md_to_pdf


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to PDF",
        prog="md2pdf"
    )
    parser.add_argument(
        "input",
        help="Input Markdown file"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output PDF file (default: same name as input with .pdf extension)"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{args.input}' not found", file=sys.stderr)
        return 1
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = input_path.with_suffix('.pdf')
    
    try:
        convert_md_to_pdf(str(input_path), str(output_path))
        print(f"Successfully converted '{input_path}' to '{output_path}'")
        return 0
    except Exception as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
