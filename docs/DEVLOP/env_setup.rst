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

All tools are recommended to be installed in a **virtual environment**, usually set by `virtualenv`_.

They should be installed properly by either ``pip-3.3 install <package>`` or ``easy_install-3.3 <package>``.

Installing from zipped source file through pip is possible. Take `numpydoc`_ as example,

.. code-block:: bash

    wget https://github.com/numpy/numpydoc/archive/master.zip
    pip-3.3 install master.zip

