from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    LONG_DESC = f.read()

with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    VERSION = f.read().strip()

setup(
    name='nextbiopy',
    version=VERSION,

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
