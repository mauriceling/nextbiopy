########################
Python 2.7 Compatibility
########################

Issues
======

Unicode and Bytestring
----------------------

Iterator
--------
In 3.x ``self.__next__()`` is called; in 2.x ``self.next()`` is called. To make 2.x compatible,

.. code-block:: python

    class MyIterator(object):
        
        def __next__(self):
            return next(some_iterator)

        def next(self):
            return self.__next__()


*New-style* Class
-----------------
In 3.x, only new-style class exists. While in 2.x, one should use

.. code-block:: python

    class Myclass(object):
        pass

to assert it is a new style class.


Supplement Fuctions in :mod:`nextbiopy.compat`
===============================================

.. automodule:: nextbiopy.compat

.. autodata:: PY2
