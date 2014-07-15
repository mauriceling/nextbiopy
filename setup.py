from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    LONG_DESC = f.read()

def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return open(path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='nextbiopy',
    version=find_version('nextbiopy', '__init__.py'),

    license='MIT',
    description='Next bio python library',
    long_description=LONG_DESC,

    author='Liang Bo Wang',
    author_email='b98901114@ntu.edu.tw',

    url='https://github.com/nextbiopy/nextbiopy',
    classifiers=[
        'Development Status :: 1 - Planning',

        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',

        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],

    keywords='ngs',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    test_suite='nose.collector',
)
