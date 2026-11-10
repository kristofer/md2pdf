"""CLI tests for md2pdf."""

import contextlib
import io
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

# md2pdf.converter imports weasyprint/markdown at module load; stub them so
# these CLI validation tests run without the native PDF toolchain.
_weasyprint_stub = types.ModuleType("weasyprint")
_weasyprint_stub.HTML = object
sys.modules.setdefault("weasyprint", _weasyprint_stub)
_markdown_stub = types.ModuleType("markdown")
_markdown_stub.markdown = lambda text, **kwargs: text
sys.modules.setdefault("markdown", _markdown_stub)

from md2pdf.cli import main


class MissingCssFileTests(unittest.TestCase):
    def test_missing_css_file_is_clean_error(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / "doc.md"
            input_path.write_text("# Title\n", encoding="utf-8")
            missing = str(Path(temporary_directory) / "nope.css")

            err = io.StringIO()
            with patch("md2pdf.cli.convert_md_to_pdf") as convert, patch(
                "sys.argv", ["md2pdf", str(input_path), "-c", missing]
            ), contextlib.redirect_stderr(err):
                self.assertEqual(main(), 1)
                convert.assert_not_called()

            self.assertIn("nope.css", err.getvalue())

    def test_existing_css_file_is_forwarded(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / "doc.md"
            input_path.write_text("# Title\n", encoding="utf-8")
            css_path = Path(temporary_directory) / "style.css"
            css_path.write_text("body {}\n", encoding="utf-8")

            with patch("md2pdf.cli.convert_md_to_pdf") as convert, patch(
                "sys.argv", ["md2pdf", str(input_path), "-c", str(css_path)]
            ):
                self.assertEqual(main(), 0)
                convert.assert_called_once()

            _, kwargs = convert.call_args
            self.assertEqual(kwargs["css_files"], [str(css_path)])


if __name__ == "__main__":
    unittest.main()
