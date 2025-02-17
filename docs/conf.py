# Configuration file for the Sphinx documentation builder.

extensions = [
    "myst_parser",  # Enables Markdown support
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode"
]

# Recognize Markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
