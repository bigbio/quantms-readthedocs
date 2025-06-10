# ![nf-core/quantms](docs/images/nf-core-quantms_logo_light.png#gh-light-mode-only) ![nf-core/quantms](docs/images/nf-core-quantms_logo_dark.png#gh-dark-mode-only)

Sphinx documentation for the bigbio/quantms pipeline.

## Docs creation

The documentation is built by ReadTheDocs and you can see previews of your changes for
a PR specific build, see the
[ReadTheDocs project builds](https://readthedocs.org/projects/quantms-readthedocs/builds/).
There is under the Actions tab in a PR also a direct link to the ReadTheDocs build for that PR.

### local build

In order to build the docs you need to 

  1. install sphinx and additional support packages
  2. build the package reference files
  3. run sphinx to create a local html version

Install the docs dependencies of the package (as speciefied in toml):

```bash
# in main folder
pip install -r requirements.txt
```

Then build the html page using Sphinx command line tools.
The command needs to be run from within the `docs` folder.

```bash	
# build page in docs folder
sphinx-build -n -W --keep-going -b html ./ ./_build/
```
