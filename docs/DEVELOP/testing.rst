#######
Testing
#######

It's important to write tests for your code.

If you are new to testing or unit test, one is encouraged to read
`Tests on Python-Guide <http://docs.python-guide.org/en/latest/writing/tests/>`__.

In our policy, **code with test coverage < 80% cannot be merged**. So all codes should come along with their tests.

.. _testing:

Running Tests
=============

.. note::
    We need help on implementing ``import numpy as np; np.test()`` testing.
    See the `issue <https://github.com/nextbiopy/nextbiopy/issues/4>`__ on Github.

Make sure to run test every time messing with source code.

Currently one should install from git repo,
see :ref:`Installing from Git <install_git>` and :ref:`build_develop_env`.

In source code directory, both two commands run tests through nose.

.. code-block:: bash

    $ nosetests-3.3
    # .........
    # ----------------------------------------------------------------------
    # Ran 9 tests in 0.023s
    # 
    # OK

.. code-block:: bash

    $ python3 setup.py test
    # running test
    # ... (trimmed) ...

If any test fails, it prints the test name and the error message below.

.. note:: **Pass all tests** before you send your PR


.. _coverage:

Get Coverage of Test
====================

Writing tests are sometimes boring and human is always lazy,
so we often forget to write tests.

To see how many line of the code has been tested, one run the test coverage.

Since `coverage <http://nedbatchelder.com/code/coverage/>`__ is well integrated with nose,
a coverage report can be made by given extra argument ``--with-coverage`` to nosetests.

.. code-block:: bash

    nosetests-3.3 --with-coverage
    # .........
    # Name                 Stmts   Miss  Cover   Missing
    # --------------------------------------------------
    # nextbiopy                2      0   100%
    # nextbiopy._version       1      0   100%
    # nextbiopy.core          30      5    83%   26, 157-160, 164
    # --------------------------------------------------
    # TOTAL                   33      5    85%
    # ----------------------------------------------------------------------
    # Ran 9 tests in 0.047s
    #
    # OK

Those lines of code without being tested will be collected in column *Missing*.

Make HTML Report
----------------

A HTML report highlighting those no-tested lines can be made by argument ``--cover-html``.

.. code-block:: bash

    nosetests-3.3 --with-coverage --cover-html

The html report will be at ``/cover/index.html``.

.. note:: **Coverage > 80%** before you send your PR.



Write Your Tests
================

see package `nose <http://nose.readthedocs.org/en/latest/>`__ and 
module :py:mod:`unittest` of Python standard library to write your own tests.

Tests are put in a folder ``test`` under the module you test, 
and its filename should start with ``test_``.

For example,

- test for ``nextbiopy/core.py`` goes to ``nextbiopy/test/test_core.py``
- test for ``nextbiopy/io/fasta.py`` goes to ``nextbiopy/io/test/test_fasta.py``

And nose provides a way to test a specific case, using Python path rule.

.. code-block:: bash

    nosetests-3.3 -v nextbiopy                                      # only this module
    nosetests-3.3 -v nextbiopy.test.test_core                       # only this test file
    nosetests-3.3 -v nextbiopy.test.test_core.TestCoreFormatError   # only this unittest case
