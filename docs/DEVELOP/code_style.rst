##########
Code Style
##########

.. seealso::
    One is encouraged to read `Code Style section on Python-Guide <http://docs.python-guide.org/en/latest/writing/style/>`__ first.

We follows :pep:`8` and tries to fully conform to it.

However, syntax errors W2, W3, E3 can be ignored.

+------------+----------------------+
| Error Code | Error Message        |
+============+======================+
| W2         | Whitespace warning   |
+------------+----------------------+
| W3         | Blank line warning   |
+------------+----------------------+
| E3         | Blank line           |
+------------+----------------------+

More error code description can be found at `here <http://pep8.readthedocs.org/en/latest/intro.html#error-codes>`__.


Check Syntax using Linter
=========================

A syntax checker, so-called linter, will check whether your code following all rules.

We recommend packages `pep8`_, `pyflakes`_, or `flake8`_, a combined of first two.

.. _pep8: https://github.com/jcrocholl/pep8
.. _pyflakes: https://launchpad.net/pyflakes
.. _flake8: http://flake8.readthedocs.org/en/2.0/

For ``flake8`` use case,

.. code-block:: bash

    flake8 --ignore=E3,W3,W2 --max-complexity 12 core.py


Special Cases
=============

``__init__.py``
---------------

``__init__.py`` often triggers many error messages
because it imports some module but never uses them.

.. code-block:: bash

    flake8 --ignore=E3,W3,W2 --max-complexity 12 __init__.py
    #__init__.py:4:1: F401 '__version__' imported but unused
    #__init__.py:5:1: F401 'FormatError' imported but unused
    #__init__.py:5:1: F401 'Seq' imported but unused

