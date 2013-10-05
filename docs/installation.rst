############
Installation
############


Quick Install
=============

Nextbiopy requires **Python 3.3+, 2.7, or pypy 1.9**.

From PyPI
---------

.. warning:: Currently **NOT** supported

.. code-block:: bash

    pip3 install nextbiopy


From Zipped Source
------------------

Download the zipped source file from `here`__,
use `pip`_ to install.

.. code-block:: bash

    wget https://github.com/nextbiopy/nextbiopy/archive/master.zip
    pip3 install master.zip

.. _pip: www.pip-installer.org/
__ https://github.com/nextbiopy/nextbiopy/archive/master.zip

.. note::
    Since NextBiopy are still in early phase of development,
    currently we recommend to use :ref:`installation from git <install_git>`.

.. _install_git:

From Git
--------
.. code-block:: bash

    git clone https://github.com/nextbiopy/nextbiopy.git
    cd nextbiopy
    python3 setup.py install


.. _dependencies:

Finally, check the installation by

.. code-block:: python

    >>> import nextbiopy as nb
    >>> print(nb.__version__)


Dependencies
============

Required
--------

Generally NextBiopy requires the following packages:

- `Numpy`_
- `pandas`_

.. _Numpy: http://www.numpy.org/
.. _pandas: http://pandas.pydata.org/

Optional
--------

- `nose`_ for unit testing

.. _nose: http://nose.readthedocs.org/
