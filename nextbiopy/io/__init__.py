"""I/O to all external file format.

Currently it supports the following file types.

+------------------------------------------+------+-------+------------------+
| File Type                                | Read | Write | Note             |
+==========================================+======+=======+==================+
| FASTA (:class:`~nextbiopy.io.Fasta`)     | Y    | N     |                  |
+------------------------------------------+------+-------+------------------+

"""
# flake8: noqa
from nextbiopy.io._fastaq import Fasta
