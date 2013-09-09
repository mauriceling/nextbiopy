*********
NextBiopy
*********

Your next bio Python library.

Dependencies
============

NextBiopy depends on the following packages:

- `Numpy`_
- `pandas`_

.. _Numpy: http://www.numpy.org/
.. _pandas: http://pandas.pydata.org/


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

We host the documentation on `readthedocs <nextbiopy.rtfd.org>`_.


Contributing
============

Please refer to this documentation `page`__.

__ http://nextbiopy.readthedocs.org/en/latest/DEVLOP/development.html


Bug Report and Feature Request
==============================

Please use GitHub issue. 
