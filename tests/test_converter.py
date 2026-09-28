import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from md2pdf.converter import convert_md_to_pdf


class ConvertMarkdownToPdfTests(unittest.TestCase):
    def test_resolves_relative_images_from_markdown_directory(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            document_directory = Path(temporary_directory) / "documents"
            document_directory.mkdir()
            input_path = document_directory / "report.md"
            input_path.write_text("![Chart](images/chart.png)", encoding="utf-8")
            output_path = Path(temporary_directory) / "report.pdf"

            with patch("md2pdf.converter.HTML") as html:
                convert_md_to_pdf(input_path, output_path)

            html.assert_called_once()
            self.assertEqual(
                html.call_args.kwargs["base_url"],
                str(document_directory.resolve()),
            )
            html.return_value.write_pdf.assert_called_once_with(output_path)


if __name__ == "__main__":
    unittest.main()