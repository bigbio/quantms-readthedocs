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
import tempfile
import subprocess
import shutil
from pathlib import Path

# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "quantms"
copyright = "2022, daichengxin, jpfeuffer, timosachenberg, ypriverol"
author = "daichengxin, jpfeuffer, timosachenberg, ypriverol"

# The full version, including alpha/beta/rc tags
release = "1.7.0"

# Language for this documentation
language = "en"

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
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

numfig = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom CSS files to include
html_css_files = [
    "custom.css",
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


# -- Generating nf-docs ------------------------------------------------------

PIPELINE_GIT = os.environ.get(
    "PIPELINE_GIT", "https://github.com/bigbio/quantms.git"
)  # quantMS repo URL
PIPELINE_REF = os.environ.get("PIPELINE_REF", "master")  # branch
GENERATED_DIRNAME = "_nf_docs"  # folder with generated docs


def generate_nf_docs(app):
    srcdir = Path(app.srcdir)
    outdir = srcdir / GENERATED_DIRNAME
    # avoid re-generating repeatedly
    if outdir.exists():
        shutil.rmtree(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    tmp = Path(tempfile.mkdtemp(prefix="nfdocs-"))
    try:
        # clone only the ref
        subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "--branch",
                PIPELINE_REF,
                PIPELINE_GIT,
                str(tmp),
            ],
            check=True,
        )
        # run nf-docs CLI command
        subprocess.run(["nf-docs", "generate", str(tmp)], check=True)
        # move generator output into ReadTheDocs source directory
        generated_from_tmp = tmp / "site"
        if generated_from_tmp.exists():
            shutil.move(str(generated_from_tmp), str(outdir))
        else:
            # fallback: move all files generated in tmp into outdir
            for p in tmp.iterdir():
                if p.name == ".git":
                    continue
                shutil.move(str(p), str(outdir / p.name))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def setup(app):
    app.connect("builder-inited", generate_nf_docs)


html_extra_path = [GENERATED_DIRNAME]
