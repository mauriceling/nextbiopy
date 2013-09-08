'''NextBiopy, a bio python utility library

'''
from nextbiopy._version import __version__

from nextbiopy.core import Seq
NO_NOSE_MSG = """\
Testing NextBiopy require Python package nose, which can be installed by

    $ pip install nose

Cannot import package nose, abort testing.
"""

try:
    from nose import main as test
except ImportError:
    def _exit_no_nose():
        import sys
        sys.exit(NO_NOSE_MSG)
    test = _exit_no_nose

