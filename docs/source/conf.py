# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import importlib.metadata
import time

# -- Project information -----------------------------------------------------
# Change these for your project.
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

# Read from the installed package, so it matches the release.
release = importlib.metadata.version("example_package")

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "autoapi.extension",
]

# Napoleon: Google-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_ivar = True

# API reference generated from the source by sphinx-autoapi
autoapi_dirs = ["../../example_package"]
autoapi_root = "reference"
autoapi_add_toctree_entry = False
autoapi_member_order = "groupwise"
# Include the __init__ docstring, where the constructor arguments are documented
autoapi_python_class_content = "both"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
]

# Show type hints in the parameter list rather than the signature
autodoc_typehints = "description"
add_module_names = False
python_maximum_signature_line_length = 88

templates_path = ["_templates"]

source_suffix = ".rst"
master_doc = "index"
language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# The shared CCPBioSim theme. Change github_repo to your repository's name.
html_theme = "ccpbiosim_sphinx_theme"
html_context = {"github_repo": "Python-Template"}
html_static_path = ["_static"]
