# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Run Python'
author = 'ADM'
release = '2025'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinxcontrib.bibtex',
    'sphinx_multitoc_numbering',
    'myst_nb'
]

# Suppress specific warnings
suppress_warnings = [
    'etoc.toctree',
    'epub.unknown_project_files',
    'image.nonlocal_uri',
    'ref.ref',
    'myst.header',
    'mystnb.exec'
]

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'

# -- Options for LaTeX output ------------------------------------------------
latex_documents = [
    ('index', 'book.tex', 'Run Python Documentation', 'ADM', 'manual'),
]

# -- Additional options ------------------------------------------------------
# You can add any additional Sphinx options here if needed.
