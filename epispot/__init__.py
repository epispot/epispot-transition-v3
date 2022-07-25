"""
.. include:: ../README.md
<!-- 
Documentation available at: 
https://epispot.github.io/epispot/en/v3.0.0-alpha-3 
-->
"""


def dependency_check():
    """Checks dependencies"""
    try:
        import numpy
    except ImportError:  # pragma: no cover
        raise ImportError('In order to integrate `epispot` models, '
                          '`numpy` is a required dependency.\n'
                          'Install with either:\n'
                          ' $ pip install epispot\n'
                          ' $ conda install epispot')
    try:
        import matplotlib  # lgtm [py/import-and-import-from]
    except ImportError:  # pragma: no cover
        raise ImportError('In order to display plots, `matplotlib` is '
                          'a required dependency.\n'
                          'Install with either:\n'
                          ' $ pip install matplotlib\n'
                          ' $ conda install matplotlib')


# imports
import warnings
import random
import dill


# dependencies
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors


# helper funcs
def _check_versions():
    """Checks for version conflicts"""
    pass

def _check_install():  # pragma: no cover
    """Checks for installation errors"""
    raise RuntimeError(
        'It seems that this installation of epispot '
        + 'may have been corrupted.\n'
        + 'Please check for the latest version of epispot listed here:\n'
        + 'https://pypi.org/project/epispot/\n'
    )

def _check_updates():
    """Checks for updates"""
    pass


# global funcs
def sanity_check():
    """
    Sanity check to check for basic installation errors, 
    version conflicts, upgrades, etc.

    **Run this if you experience any problems with epispot and before 
    submitting any issues**
    
    """
    # check for installation errors
    if not source or not version:  # pragma: no cover
        _check_install()

    # check for version conflicts
    import sys
    if (sys.version_info[0] < 3) or \
       (sys.version_info[0] == 3 and sys.version_info[1] < 7):
        raise RuntimeError('epispot requires Python 3.7 or later')  # pragma: no cover
    _check_versions()

    # check for updates
    _check_updates()

def __cite__(bibtex=False):
    """
    Returns the citation string for the package.
    Use `bibtex=True` to return the BibTeX-formatted citation.
    """
    if bibtex:
        return '''@software{q9i_2021_4624423,
  author       = {quantum9innovation},
  title        = {epispot/epispot:},
  month        = apr,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {2.1.1},
  doi          = {10.5281/zenodo.4624423},
  url          = {https://doi.org/10.5281/zenodo.4624423}
}'''
    else:
        return 'quantum9innovation (2021, April 2). epispot/epispot: (Version 2.1.1). Zenodo. <http://doi.org/10.5281/zenodo.4624423>'


# version info
version = '3.0.0'
"""
epispot's version info (updated every release)\n
Check version information with:

```
    >>> print(epispot.version)
```

Version information is also available through the `__version__` 
property, included for legacy support.
"""
__version__ = version  # alias for version

stable = False
"""
Build stability:

- True ⇒ main package (stable)
- False ⇒ nightly (unreleased) package (possibly unstable)
"""


# local
from . import comps
from . import estimates
from . import models
from . import params
from . import plots
from . import pre


# metadata
source = 'https://www.github.com/epispot/epispot'
"""URL to VCS source"""
raw = f'https://raw.githubusercontent.com/epispot/epispot/v{version}/'
"""URL to raw VCS source (must append file path)"""
docs = f'https://epispot.github.io/epispot/en/v{version}/'
"""Project documentation (version-specific)"""
issues = 'https://www.github.com/epispot/epispot/issues'
"""Bug tracker"""
citation = __cite__()
"""Static citation string"""
