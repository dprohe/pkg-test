# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import re


def get_version():
    VERSIONFILE = os.path.join("..", "..", "..", "pyproject.toml")
    with open(VERSIONFILE, "rt") as f:
        lines = f.readlines()
    vgx = "version = '[0-9+.0-9+.0-9+]*[a-zA-Z0-9]*'"
    for line in lines:
        mo = re.search(vgx, line, re.M)
        if mo:
            return mo.group().split("'")[1]
    raise RuntimeError("Unable to find version in %s." % (VERSIONFILE,))


project = "pkg-test2"
copyright = "2026, dprohe"
author = "dprohe"
version = get_version()
release = version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_title = "Test Package Documentation v" + version
html_theme_options = {
    "repository_url": "https://github.com/dprohe/pkg-test",
    "use_repository_button": True,
}
