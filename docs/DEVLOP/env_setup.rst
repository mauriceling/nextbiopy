##############################
Set up Development Environment
##############################

Prequisites
===========

Besides mentioned in :ref:`Prequisites for Installation <prequisites>`, extra packages are needed for development.

**Syntax Checker (Linter)**

- `pep8`_
- `pyflakes`_
- or `flake8`_, a wrapped package containing both.

**Virtual Enviroment**

- `virtualenv`_

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

.. _nose: http://nose.readthedocs.org/
.. _coverage: https://pypi.python.org/pypi/coverage
.. _tox: http://testrun.org/tox/latest/

.. _Sphinx:
.. _numpydoc: https://github.com/numpy/numpydoc
.. __: numpydoc_


Build up the Environemnt
========================

It is recommended to createn a **virtual environment**, usually set by `virtualenv`_.

.. code-block:: bash

    $ pip-3.3 install virtualenv
    $ virtualenv-3.3 VENV_nextbiopy
    $ source VENV_nextbiopy/bin/activate
    (VENV_nextbiopy)$ which pip-3.3
    # /path/to/venv/bin/pip-3.3
    (VENV_nextbiopy)$ deactivate
    $

So the development is isolated and let the system Python environment unaffected.

Then each package can be installed properly by either ``pip-3.3 install <package>`` or ``easy_install-3.3 <package>``.

It is possible to install zipped source file through pip.

Take `numpydoc`_ as example,

.. code-block:: bash

    wget https://github.com/numpy/numpydoc/archive/master.zip
    pip-3.3 install master.zip


Build NextBiopy linked to source
--------------------------------

Keep rebuilding from source is tedious, though that is the mosted clean way.

In most cases, we can build the source **in-place** without copying everything into ``site-packages``,
so it reflects the code change after reloading it.

.. code-block:: bash

    # recommended in a virtual env
    python3 setup.py develop

.. note:: version number won't change unless you trigger ``setup.py`` again.
