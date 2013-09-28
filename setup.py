import sys
import warnings
import re

#------------------------------------------------------------------------------
# Python Version Dection
#------------------------------------------------------------------------------
# arguments of 3.x specific for setuptools
setup_kwargs = {}
if sys.version_info >= (3,):
    setup_kwargs['use_2to3'] = False

#------------------------------------------------------------------------------
# Setuptools
#------------------------------------------------------------------------------
SETUPTOOLS_MSG = """\
{:s}
Try download and install it using official script ez_setup.py.
For more infomation, see setuptools site:
    http://pythonhosted.org/setuptools/index.html
"""
# require setuptools >= 0.9
try:
    import pkg_resources
    try:
        pkg_resources.require("setuptools>=0.9")
    except pkg_resources.VersionConflict:
        print(
            SETUPTOOLS_MSG.format("Require newer setuptools (>= 0.9).")
        )
        from ez_setup import use_setuptools
        use_setuptools(version="0.9.6")
except ImportError:
    print(
        SETUPTOOLS_MSG.format("No setuptools installed.")
    )
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup

# Python version check, currently supports 3.3 and up
PYTHON_2_MSG = """\
Require Python 3.3 and up, currently 2.x not supported.
However, we are planned to port it back to 2.7 and we are asking for HELP!
Please help this issue:
    https://github.com/nextbiopy/nextbiopy/issues/1
"""

if sys.version_info < (3, 3):
    sys.exit(PYTHON_2_MSG)


#-----------------------------------------------------------------------------
# Package Information
#-----------------------------------------------------------------------------
MAJOR = 0
MINOR = 0
MICRO = 1
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
QUALIFIER = ''       # something like rc1, rc2

AUTHOR = 'Liang Bo Wang'
AUTHOR_EMAIL = 'b98901114@ntu.edu.tw'
MAINTAINER = 'Liang Bo Wang'
MAINTAINER_EMAIL = 'b98901114@ntu.edu.tw'
URL = 'https://github.com/nextbiopy/nextbiopy'
DESCRIPTION = 'Next bio python library'
LONG_DESC = """\
**NextBiopy** is a Python package providing basic, fast, and flexible data
structure to store file formats widely-used in Biology.

NextBiopy aims to support the following file format:

  - FASTA/Q
  - BAM/SAM (using `PySAM <https://code.google.com/p/pysam/>`__)
"""
LICENSE = "MIT"
CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.3',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research'
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
]


#-----------------------------------------------------------------------------
# Version Management
#-----------------------------------------------------------------------------
# This section of code is adapted from the pandas project
# (https://github.com/pydata/pandas)
# which have been permitted for use under the BSD license.
PTH_VERSION_PY = "nextbiopy/_version.py"

FULLVERSION = VERSION
GIT_VER_CMD = ["git", "describe", "--tags", "--always"]

VERSION_PY = """\
# This file is originally generated from Git information by running
#     $ python3 setup.py --version
# Distribution tarballs contain a pre-generated copy of this file.

__version__ = '{:s}'
"""

def write_version_py():
    # write version to _version.py
    with open(PTH_VERSION_PY, 'w') as f:
        f.write(VERSION_PY.format(FULLVERSION))

def read_version_py():
    try:
        for line in open(PTH_VERSION_PY):
            mo = re.match("__version__ = '([^']+)'", line)
            if mo:
                ver = mo.group(1)
                return ver
        return None
    except EnvironmentError:
        return None


def set_full_version(full_version=FULLVERSION):
    if not ISRELEASED:
        full_version += '.dev'
        import subprocess
        try:
            p = subprocess.Popen(
                GIT_VER_CMD,
                stdout=subprocess.PIPE
            )
        except OSError:
            # msysgit compatibility
            p = subprocess.Popen(
                GIT_VER_CMD,
                stdout=subprocess.PIPE
            )
        rev = p.communicate()[0]
        if p.returncode == 0:
            if sys.version_info[0] >= 3:
                rev = rev.decode('utf8')
            full_version = rev.rstrip().lstrip('v')
        else:
            warnings.warn("Couldn't get git revision, try _version.py")
            ver = read_version_py()
            if ver is not None:
                print("use %s from _version.py, may be incorrect" % ver)
                full_version = ver
            else:
                warnings.warn("version info not found, use ambiguous one")
    else:
        full_version += QUALIFIER
    return full_version

FULLVERSION = set_full_version()
write_version_py()

#-----------------------------------------------------------------------------
# Unit Test using nose
#-----------------------------------------------------------------------------
setup_kwargs["test_suite"] = "nose.collector"


#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------
setup(
    name='nextbiopy',
    packages=[
        'nextbiopy',
        'nextbiopy.core',
        'nextbiopy.io',
    ],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },
    zip_safe=False,     # may contain C extension
    # metadata for PyPI
    license=LICENSE,
    version=FULLVERSION,
    description=DESCRIPTION,
    long_description=LONG_DESC,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url=URL,
    classifiers=CLASSIFIERS,
    platforms='any',
    **setup_kwargs
)
