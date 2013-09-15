#################
Developers' Guide
#################

We are asking for help if anyone is interested in making next-generation sequencing analysis easier in Python.

How to Contribute?
==================

There are many ways to help us. From bug report to code submits, even discussion or advice will help us a lot.

Bug Report
----------

Simply running tests on your environment, see :ref:`testing`. If any error is reported, create an issue on
`Github <https://github.com/nextbiopy/nextbiopy/issues>`__.

In a issue it should contain

- Your system environment (Windows, Mac OS X, or Linux Distribution)
- NextBiopy version (try upgrade to the newest see if the bug has been disappeared)
- A **reproducible** minimal code which has unexpected result

So others can get into the situation quickly and give you a hand.

Documentation
-------------

We write our documentation in `reStructuredText <http://docutils.sourceforge.net/rst.html>`__
(reST or rst in short) format, and generate documentations using `Sphinx <http://sphinx-doc.org/>`__. Documentation has two parts: non-API and API, which are stored in different places. The following explains how to contribute to these parts respectively.

**Non-API Doc**

Docs of this part are stored in ``/docs``, the quickest way to pick up is by reading the existing documentation (files with ``.rst`` extension).

**API Doc**

These docs are generated from the `docstring <http://en.wikipedia.org/wiki/Docstring#Python>`__ inside code. For example, API doc for :class:`~nextbiopy.core.Seq` is generated from the docstring of :class:`~!nextbiopy.core.Seq` itself.

.. code-block:: python3

    class Seq():
        """Core class storing one sequence record.

        This class is the base class storing information about sequences.
        For example, a FASTA file contains mutliple sequence record.

        ... (trimmed) ...

        Examples
        --------
        Creat a sequence instance is easy.

            >>> s = Seq('name', 'ATCG')
            >>> s
            Seq(name='name', seq='ATCG', qual=None)

        ... (trimmed) ...
        """

        def __init__(self, name, seq, qual=None):
            """ Create an instance of a sequence record.

            Parameters
            ----------
            name : string
            seq : string
            qual : string, optional

            ... (trimmed) ...
            """

Usually developers are not willing to spend too much time refining their docstring, so it is welcomed to improve them!

.. seealso::
    :ref:`docstring_style` for more information.


Contributing Code
-----------------

Contributing codes requires some steps to follow, which are detailed in docs linked in the end.
However it can be summed up as

1. Write your code
2. Add tests if needed (for example, add new functions or classes)
3. Pass all tests and total coverage should exceeds 80%
4. Complete your docstring (at least short descriptions. Examples are nice!)
5. Check your code if they follow the coding style
6. Submit your code by sending us a pull request (PR) (see if your PR pass Travis CI)
7. Keep an eye on your PR page, others may feedback your code.
8. *Hooray!* Wait to be merged!

If you are new to open source project, some terms may confuse you. For example, what's the code style? How to write unit test? How to make a PR?

So the following links will take you into the details of contributing steps.

.. toctree::
   :maxdepth: 2

   env_setup
   code_style
   doc_string_style
   testing
   conventions
   release_version


.. seealso::
    As a good start, `Python Guide <http://docs.python-guide.org/en/latest/>`__,
    also known as *The Hitchhiker's Guide to Python*, serves as a good practice of Python development How-To.

    One is highly recommended to follow this site being the first time.

FAQ
===

1.  **Q:** I am not an English native speaker, can I use Chines or Japanese instead?

    **A:** We use **English** in discussion.

    Though most people here are from non-English-native countries,
    using English could help others join our discussion.

    If you find yourself trouble using English,
    it would be fine to put your words in Japanese or Chinese again,
    and let others check whether they means the same.

    For example,

    .. code-block:: none

        We could put all utility functions for Unincode of Python 2.7 in a separate module.
        Because it is often used, so we should discuss
        what module names would best expressed its function ?
        ----
        我們要不要把 Python 2.7 中 Unicode 相關處理的函式放在一個獨立的 module 中？
        因為它蠻常用的，也許我們可以投票一下決定什麼名字比較好？

