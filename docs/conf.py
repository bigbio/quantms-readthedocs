# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'quantms'
copyright = '2022, daichengxin, jpfeuffer, timosachenberg, ypriverol'
author = 'daichengxin, jpfeuffer, timosachenberg, ypriverol'

# The full version, including alpha/beta/rc tags
release = '1.7.0'

# Language for this documentation
language = 'en'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_new_tab_link",
    "myst_nb",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

numfig = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom CSS files to include
html_css_files = [
    'custom.css',
]

if os.environ.get("READTHEDOCS") == "True":
    # If we are building on ReadTheDocs, we need to download the output file
    # from the GitHub repository.
    def download_files(_):
        from setup_docs import download_output

        # Download the output file
        download_output()

    def setup(app):
        # on extensions, see:
        # https://www.sphinx-doc.org/en/master/usage/extensions/index.html
        app.connect("builder-inited", download_files)
