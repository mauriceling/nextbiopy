import sys

# arguments of 3.x specific for setuptools
setup_kwargs = {}
if sys.version_info >= (3,):
    setup_kwargs['use_2to3'] = False

# require setuptools >= 0.9
import pkg_resources
try:
    pkg_resources.require("setuptools>=0.9")
except pkg_resources.VersionConflict:
    from ez_setup import use_setuptools
    use_setuptools(version="0.9.6")
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

__version__ = '0.0.0'

setup(
    name='nextbiopy',
    packages=['nextbiopy'],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },
    zip_safe=False,     # may contain C extension
    # metadata for PyPI
    license='MIT',
    version=__version__,
    description='Next bio python utility library',
    author='Liang Bo Wang',
    author_email='b98901114@ntu.edu.tw',
    maintainer='Liang Bo Wang',
    maintainer_email='b98901114@ntu.edu.tw',
    url='https://github.com/nextbiopy/nextbiopy',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
    ],
    **setup_kwargs
)
