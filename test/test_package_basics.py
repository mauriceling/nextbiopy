from nose.tools import ok_
import re

def test_version_validity():
    import nextbiopy as nb
    ok_(re.match("^\d+.\d+.\d+($|-\d+-.{8}$)", nb.__version__),
        msg="Unexpected version number: {:s}".format(nb.__version__))

## Run tests using nose
# at root path to package, for example,
#
# $ cd ~/nextbiopy
# $ nosetests-3.3
# # .
# # ----------------------------------------------------------------------
# # Ran 1 test in 0.004s
# #
# # OK

## Run test using nose with coverage
# First, one need to install package ``coverage``
#
# $ pip-3.3 install coverage
# $ nosetest-3.3 --with-coverage
# # .
# # Name                 Stmts   Miss  Cover   Missing
# # --------------------------------------------------
# # nextbiopy                1      0   100%
# # nextbiopy._version       1      0   100%
# # --------------------------------------------------
# # TOTAL                    2      0   100%
# # ----------------------------------------------------------------------
# # Ran 1 test in 0.010s
# #
# # OK
