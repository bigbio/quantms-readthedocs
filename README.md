# ![nf-core/quantms](docs/images/nf-core-quantms_logo_light.png#gh-light-mode-only) ![nf-core/quantms](docs/images/nf-core-quantms_logo_dark.png#gh-dark-mode-only)

Source repository for the Sphinx documentation of the `bigbio/quantms` Nextflow pipeline.

## Docs Creation

The documentation is built by ReadTheDocs. You can see previews of your changes for
a PR-specific build on
[ReadTheDocs project builds](https://readthedocs.org/projects/quantms-readthedocs/builds/),
and under the Actions tab of this PR.

### Local Build

In order to build the docs, you need to 

  1. Install sphinx and additional support packages
  2. Build the package reference files
  3. Run sphinx to create a local html version

Install the docs dependencies of the package (as specified in `requirements.txt`):

```bash
# in main folder
pip install -r requirements.txt
```

Run the following command inside the `docs` folder to build the HTML:

```bash
# build page in docs folder
sphinx-build -n -W --keep-going -b html ./ ./_build/
```
