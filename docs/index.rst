#######################################
NextBiopy: your next bio Python library
#######################################

.. image:: https://api.travis-ci.org/nextbiopy/nextbiopy.png?branch=master,develop
    :target: https://travis-ci.org/nextbiopy/nextbiopy
.. image:: https://coveralls.io/repos/nextbiopy/nextbiopy/badge.png?branch=develop
    :target: https://coveralls.io/r/nextbiopy/nextbiopy

**Version**: |version|

**Last update**: |today|

.. note::

    **A Sprint! will be on Oct. 5 in Taipei**.

    Many Nextbiopy's developers are gathering to solve LARGE issues
    and significant progess is highly expected.

    If you want to join us, go register `here <http://registrano.com/events/9691cb>`__.
    Some draft plan is on `gist <https://gist.github.com/ccwang002/6272392>`__ (Mandarin).

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

