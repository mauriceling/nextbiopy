*********
NextBiopy
*********

.. image:: https://api.travis-ci.org/nextbiopy/nextbiopy.png?branch=master,develop
    :target: https://travis-ci.org/nextbiopy/nextbiopy
.. image:: https://coveralls.io/repos/nextbiopy/nextbiopy/badge.png?branch=develop
    :target: https://coveralls.io/r/nextbiopy/nextbiopy

Your next bio Python library.

Dependencies
============

NextBiopy depends on the following packages:

- `NumPy`_
- `pandas`_
- `matplotlib`_

.. _NumPy: http://www.numpy.org/
.. _pandas: http://pandas.pydata.org/
.. _matplotlib: http://matplotlib.org/

Installation
============

Nextbiopy requires Python 3.3 and up. 

If you are interested in 2.7 or earlier support, please **help us** and refer to this `issue`_.

.. _issue: https://github.com/nextbiopy/nextbiopy/issues/1

Using ``pip``
-------------

Installing from PyPI is *NOT* supported yet.

Download the zipped source file from `here`__,
use `pip`_ to install.

.. _pip: www.pip-installer.org/
__ https://github.com/nextbiopy/nextbiopy/archive/master.zip

.. code-block::

    wget https://github.com/nextbiopy/nextbiopy/archive/master.zip
    pip3 install master.zip

From Git
--------

.. code-block::

    git clone https://github.com/nextbiopy/nextbiopy.git
    cd nextbiopy
    python3 setup.py install
    

Finally, check the installation by

.. code-block:: python

    >>> import nextbiopy as nb
    >>> print(nb.__version__)


License
=======

MIT


Documentation
=============

We host the documentation on `readthedocs <http://nextbiopy.rtfd.org>`_.


Contributing
============

Please refer to this documentation `page`__.

__ http://nextbiopy.readthedocs.org/en/latest/DEVELOP/development.html


Bug Report and Feature Request
==============================

Please use GitHub issue. 
