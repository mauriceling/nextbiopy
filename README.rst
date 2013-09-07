*********
NextBiopy
*********

Your next bio Python utility library.

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

.. warning:: Currently **NOT** support installing from PyPI.

.. code-block::

    pip3 install nextbiopy


But one can still use ``pip`` to install. Download the zipped source file (on ``master`` branch) from `here`__,

__ https://github.com/nextbiopy/nextbiopy/archive/master.zip


.. code-block::

    pip3 install master.zip

As long as basic feature works, we will publish to PyPI and there is no need to do by this way.

From source
-----------

.. code-block::

    git clone https://github.com/nextbiopy/nextbiopy.git
    cd nextbiopy
    python3 setup.py install
    

Test Installation
-----------------

Check the installation by

.. code-block:: python

    >>> import nextbiopy as nb
    >>> print(nb.__version__)

Unit tests will be further added.


License
=======

MIT


Documentation
=============

We host the documentation on `readthedocs <nextbiopy.rtfd.org>`_


Contributing
============

Please refer to the `wiki`__ page.

__ https://github.com/nextbiopy/nextbiopy/wiki/Contributing-and-Environment-Setup


Bug Report and Feature Request
==============================

Please use GitHub issue. 
