#######################################
NextBiopy: your next bio Python library
#######################################

.. image:: https://api.travis-ci.org/nextbiopy/nextbiopy.png?branch=master,develop
    :target: https://travis-ci.org/nextbiopy/nextbiopy
.. image:: https://coveralls.io/repos/nextbiopy/nextbiopy/badge.png?branch=develop
    :target: https://coveralls.io/r/nextbiopy/nextbiopy

**Version**: |version|

**Last update**: |today|


Introduction
============

**NextBiopy** is a Python package providing basic, fast, and flexible data structure to store file formats widely-used in Biology.

It aims to support the following file format:

  - FASTA/Q
  - BAM/SAM (using `PySAM <https://code.google.com/p/pysam/>`__)
  - VCF (using `PyVCF <https://github.com/jamescasbon/PyVCF>`__)

Underneath it extends `numpy`_ and `pandas`_ so it should be easy to import your sequence data into further data analysis.

.. _numpy: http://www.numpy.org/
.. _pandas: http://pandas.pydata.org/


Contents
========

.. toctree::
   :maxdepth: 2

   installation
   quickstart
   tutorial
   API/nextbiopy
   DEVELOP/development


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

