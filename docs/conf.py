# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys
import time

# Put the repository root on sys.path so autodoc imports the local package.
DOCS_DIR = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.abspath(os.path.join(DOCS_DIR, ".."))
sys.path.insert(0, REPO_ROOT)

# -- Project information -----------------------------------------------------
project = "CCPBioSim-Python-Template"
copyright_first_year = "2025"
copyright_owners = "CCPBioSim"
author = "CCPBioSim"

current_year = str(time.localtime().tm_year)
copyright_year_string = (
    current_year
    if current_year == copyright_first_year
    else f"{copyright_first_year}-{current_year}"
)
copyright = f"{copyright_year_string}, {copyright_owners}. All rights reserved"

version = ""
release = ""

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "nbsphinx",
    "sphinx_copybutton",
]

# Autosummary (API stubs)
autosummary_generate = True

# Napoleon: Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_ivar = True

templates_path = ["_templates"]

source_suffix = ".rst"
master_doc = "index"
language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
