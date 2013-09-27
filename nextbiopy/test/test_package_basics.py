from nose.tools import ok_
import re

def test_version_validity():
    import nextbiopy as nb
    ok_(re.match("^\d+.\d+.\d+($|-\d+-.{8}$)", nb.__version__),
        msg="Unexpected version number: {:s}".format(nb.__version__))
