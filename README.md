
[pysal/spaghetti](https://pysal-spaghetti.readthedocs.io)
=========================================================

SPAtial GrapHs: nETworks, Topology, & Inference
===============================================

*An example of snapping observation points to a network and plotting:*

![snap_plot](figs/snap_plot.png)



**Build & Versions**

[![PyPI version](https://badge.fury.io/py/spaghetti.svg)](https://badge.fury.io/py/spaghetti) [![GitHub version](https://img.shields.io/github/release/pysal/spaghetti.svg)](https://img.shields.io/github/release/pysal/spaghetti) [![Build Status](https://travis-ci.org/pysal/spaghetti.svg?branch=master)](https://travis-ci.org/pysal/spaghetti) [![Documentation Status](https://readthedocs.org/projects/pysal-spaghetti/badge/?version=latest)](https://pysal-spaghetti.readthedocs.io/en/latest/?badge=latest) [![Coverage Status](https://coveralls.io/repos/github/pysal/spaghetti/badge.svg)](https://coveralls.io/github/pysal/spaghetti)


**Anaconda**

[![Anaconda-Server Badge](https://anaconda.org/conda-forge/spaghetti/badges/version.svg)](https://anaconda.org/conda-forge/spaghetti) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/spaghetti/badges/platforms.svg)](https://anaconda.org/conda-forge/spaghetti) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/spaghetti/badges/downloads.svg)](https://anaconda.org/conda-forge/spaghetti) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/spaghetti/badges/installer/conda.svg)](https://conda.anaconda.org/conda-forge)

**Issues & Pull Requests**

[![GitHub issues open](https://img.shields.io/github/issues/pysal/spaghetti.svg?maxAge=3600)](https://github.com/pysal/spaghetti/issues) [![GitHub issues closed](https://img.shields.io/github/issues-closed/pysal/spaghetti.svg?maxAge=3600)](https://github.com/pysal/spaghetti/issues) ![Github pull requests open](https://img.shields.io/github/issues-pr/pysal/spaghetti.svg) ![Github pull requests closed](https://img.shields.io/github/issues-pr-closed/pysal/spaghetti.svg)

**Commit Activity**

![Github commit activity](https://img.shields.io/github/commit-activity/y/pysal/spaghetti.svg) ![Github commit activity](https://img.shields.io/github/commit-activity/4w/pysal/spaghetti.svg) ![Github commit activity](https://img.shields.io/github/commit-activity/w/pysal/spaghetti.svg) 


**Community & GitHub Stats**

![Github contributors](https://img.shields.io/github/contributors/pysal/spaghetti.svg) [![Gitter](https://badges.gitter.im/pysal/Spaghetti.svg)](https://gitter.im/pysal/Spaghetti?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) ![Github forks](https://img.shields.io/github/forks/pysal/spaghetti.svg?style=social&label=Forks) ![Github stars](https://img.shields.io/github/stars/pysal/spaghetti.svg?style=social&label=Stars) ![Github watchers](https://img.shields.io/github/watchers/pysal/spaghetti.svg?style=social&label=Watchers)

**Languages**

![Pypi python versions](https://img.shields.io/pypi/pyversions/spaghetti.svg) ![Github languages](https://img.shields.io/github/languages/count/pysal/spaghetti.svg) ![Github top language](https://img.shields.io/github/languages/top/pysal/spaghetti.svg)


**Licensing & Citation**

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![DOI](https://zenodo.org/badge/88305306.svg)](https://zenodo.org/badge/latestdoi/88305306)

**Misc.**

![Github search hit counter](https://img.shields.io/github/search/pysal/spaghetti/goto.svg) ![Github code size in bytes](https://img.shields.io/github/languages/code-size/pysal/spaghetti.svg) ![Github repo size in bytes](https://img.shields.io/github/repo-size/pysal/spaghetti.svg)

--------------------------------------

This package is part of a [refactoring of PySAL](https://github.com/pysal/pysal/wiki/PEP-13:-Refactor-PySAL-Using-Submodules).

--------------------------------------

Spaghetti is an open-source python library for the analysis of network-based spatial data. Originating from the `network` module in [PySAL (Python Spatial Analysis Library)](http://pysal.org), it is under active development for the inclusion of newly proposed methods for building graph-theoretic networks and the analysis of network events.

-------------------------------


Examples
--------
* [Network Usage](https://github.com/pysal/spaghetti/blob/master/notebooks/Network_Usage.ipynb)
* [Spaghetti Pointpatterns Empirical](https://github.com/pysal/spaghetti/blob/master/notebooks/Spaghetti_Pointpatterns_Empirical.ipynb)
* [Snapping Demonstration](https://github.com/pysal/spaghetti/blob/master/notebooks/Snapping_Demonstration.ipynb)
* [Facility Location](https://github.com/pysal/spaghetti/blob/master/notebooks/Facility_Location.ipynb)


Installation
------------

As of version 1.3, `spaghetti` officially supports Python [`3.6`](https://docs.python.org/3.6/) and [`3.7`](https://docs.python.org/3.7/) only. Please make sure that you are operating in a Python 3 environment.

**Installing with `conda` via [conda-forge](https://github.com/conda-forge/spaghetti-feedstock) (highly recommended)**

To install `spaghetti` and all its dependencies, we recommend using the [`conda`](https://docs.conda.io/en/latest/)
manager, specifically with the [`conda-forge`](https://conda-forge.org) channel. This can be obtained by installing the [`Anaconda Distribution`](https://docs.continuum.io/anaconda/) (a free Python distribution for data science), or through [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) (minimal distribution only containing Python and the conda package manager). 

Using `conda`, `spaghetti` can be installed as follows:
```
$ conda config --set channel_priority strict
$ conda install --channel conda-forge spaghetti
```

**Installing with [`PyPI`](https://pypi.org/project/spaghetti/)**
```
$ pip install spaghetti
```
*or* download the source distribution (`.tar.gz`) and decompress it to your selected destination. Open a command shell and navigate to the decompressed folder.
```
$ pip install .
```

***Warning***

When installing via `pip`, you have to ensure that the required dependencies for `spaghetti` are installed on your operating system. Details on how to install these packages are linked below. Using `conda` (above) avoids having to install the dependencies separately.

Install the most current development version of `spaghetti` by running:

```
$ pip install git+https://github.com/pysal/spaghetti
```


Requirements
------------
- [`esda`](https://esda.readthedocs.io/en/latest/)
- [`libspatialindex`](https://libspatialindex.org/index.html)
- [`numpy`](https://numpy.org/devdocs/)
- [`rtree`](http://toblerity.org/rtree/install.html)
- [`scipy`](http://scipy.github.io/devdocs/)

Soft Dependencies
-----------------
- [`geopandas`](http://geopandas.org/install.html)
- [`shapely`](https://shapely.readthedocs.io/en/latest/)

Contribute
----------

PySAL-spaghetti is under active development and contributors are welcome.

If you have any suggestion, feature request, or bug report, please open a new [issue](https://github.com/pysal/spaghetti/issues) on GitHub. To submit patches, please follow the PySAL development [guidelines](http://pysal.readthedocs.io/en/latest/developers/index.html) and open a [pull request](https://github.com/pysal/spaghetti). Once your changes get merged, you’ll automatically be added to the [Contributors List](https://github.com/pysal/spaghetti/graphs/contributors).

Support
-------

If you are having issues, please [create an issue](https://github.com/pysal/spaghetti/issues) or talk to us in the [gitter room](https://gitter.im/pysal/spaghetti).

License
-------

The project is licensed under the [BSD license](https://github.com/pysal/spaghetti/blob/master/LICENSE.txt).

BibTeX Citation
---------------

```
@misc{Gaboardi2018,
author = {Gaboardi, James D. and Laura, Jay and Rey, Sergio and Wolf, Levi John and Folch, David C. and Kang, Wei and Stephens, Philip and Schmidt, Charles},
month = {oct},
year = {2018},
title = {pysal/spaghetti},
url = {https://github.com/pysal/spaghetti},
keywords = {graph-theory,network-analysis,python,spatial-networks,topology}
}
```


