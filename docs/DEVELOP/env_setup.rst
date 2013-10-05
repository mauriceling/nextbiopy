##############################
Set up Development Environment
##############################

Prequisites
===========

Besides mentioned in :ref:`Prequisites for Installation <dependencies>`, extra packages are needed for development.

**Syntax Checker (Linter)**

- `pep8`_
- `pyflakes`_
- or `flake8`_, a wrapped package containing both.

**Virtual Enviroment**

- `virtualenv`_
- `virtualenvwrapper`_ *(optional)*

**Testing**

- `nose`_
- `coverage`_
- `tox`_ *(for mutli Python version)*

**Benchmark**

*Still to be determined*

**Documentation**

- `Sphinx`_
- `numpydoc`_

.. note::
    For numpydoc, download the latest version from its `project repo`__ to support Python 3.3.

.. _pep8: https://github.com/jcrocholl/pep8
.. _pyflakes: https://launchpad.net/pyflakes
.. _flake8: http://flake8.readthedocs.org/en/2.0/

.. _virtualenv: http://www.virtualenv.org/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/

.. _nose: http://nose.readthedocs.org/
.. _coverage: https://pypi.python.org/pypi/coverage
.. _tox: http://testrun.org/tox/latest/

.. _Sphinx:
.. _numpydoc: https://github.com/numpy/numpydoc
.. __: numpydoc_


Build up the Environemnt
========================

It is recommended to create a **virtual environment**, usually set by `virtualenv`_.

Create an virtual environment by

.. code-block:: bash

    $ virtualenv-3.3 venv

Use it by

.. code-block:: bash

    $ cd venv
    $ source bin/activate
    (venv)$ which pip-3.3
    # /path/to/venv/bin/pip-3.3

And leave it by

.. code-block:: bash

    (venv)$ deactivate
    $

So the development is isolated and let the system Python environment unaffected.

Then each package can be installed properly by either ``pip-3.3 install <package>`` or ``easy_install-3.3 <package>``.

It is possible to install zipped source file through pip.

Take `numpydoc`_ as example,

.. code-block:: bash

    wget https://github.com/numpy/numpydoc/archive/master.zip
    pip-3.3 install master.zip

.. _build_develop_env:

Build NextBiopy linked to source
--------------------------------

Keep rebuilding from source is tedious, though that is the most clean way.

In most cases, we can build the source **in-place** without copying everything into ``site-packages``,
so it reflects the code change after reloading it.

.. code-block:: bash

    # recommended in a virtual env
    python3 setup.py develop

.. note:: version number won't change unless you trigger ``setup.py`` again.


Manage Virtualenv Environemnt by ``virtualenvwrapper``
------------------------------------------------------

Managing multiple environments is not easy. ``virtualenvwrapper`` helps to do this job.

For supporting Python 3.x, after the installaion, one should add environemnt variable to the shell as follows::

    # For virtualenvwrapper settings
    export WORKON_HOME=$HOME/MyEnvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.3
    export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv-3.3
    source /usr/local/bin/virtualenvwrapper_lazy.sh

They could be placed in somewhere like ``~/.bash_profile`` or ``~/.zshrc``, which path to Python 3.x and virtualenv should be properly set. For more configuration please visit their official site.

Usage is easy. Make a new virtualenv is easy.

.. code-block:: bash

    mkvirtualenv nextbiopy-devel

Options to virtualenv can be passed in the same way.

.. code-block:: bash

    mkvirtualenv -p /usr/local/bin/python2.7 nextbiopy-27

Enter a virtual environment at any location

.. code-block:: bash

    workon nextbiopy-devel

Leave the virtual environment in the same way.

.. code-block:: bash

    deactivate

Test the Environment Setup
==========================

Always remember to source your virtual environment.

Source Code Linkage
-------------------

Now ``nextbiopy.__path__`` should be the path to your source code,
rather than somewhere inside ``site-packages``.

.. code-block:: python3

    >>> import nextbiopy as nb
    >>> nb.__path__
    ['/path/to/source/code/root/nextbiopy/nextbiopy']


Build Local Documentation
-------------------------

Scripts for building documentation should be properly set,
so there is no need to modify the configuration, which stores at ``docs/conf.py``.

Unix-like
^^^^^^^^^

.. code-block:: bash

    cd docs
    make html

The generated html documentation by default should be under ``_build/html``.

Windows
^^^^^^^

.. warning::
    Currently no developers are maintaining Windows version and we are **asking for help!**
    See `issue @GitHub <https://github.com/nextbiopy/nextbiopy/issues/8>`__
