"""Setup configuration for md2pdf."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="md2pdf",
    version="0.1.0",
    description="A CLI tool for converting markdown to PDFs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kristofer",
    url="https://github.com/kristofer/md2pdf",
    packages=find_packages(),
    package_data={
        "md2pdf": ["css/*.css"],
    },
    install_requires=[
        "markdown>=3.3.0",
        "weasyprint>=52.0",
    ],
    entry_points={
        "console_scripts": [
            "md2pdf=md2pdf.cli:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
