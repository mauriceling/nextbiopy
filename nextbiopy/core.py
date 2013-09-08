"""Core data structure

.. moduleauthor:: Liang Bo Wang
"""

class FormatError(Exception):
    """Base exception class for all format errror.

    Attributes
    ----------
    format_type : string, optional
        Format handling with

    msg : string, optinal
        Extra message
    """
    def __init__(self, format_type=None, msg=None):
        self.format_type = format_type
        self.msg = msg

    def __repr__(self):
        return "On handling type {:s}, {:s}".format(
            self.format_type, self.msg)

    def __str__(self):
        return self.__repr__()


class Seq():
    """Core class storing one sequence record.

    Attributes
    ----------
    name : string
        Name of the sequence

    seq : string
        Sequence

    qual : string, optional
        Quality information

    Notes
    -----
    .. warning::
        By denoting ``__slots__``, user cannot add new attribute to instances.
        However, the memory use reduces. [1]_

    .. [1] Python Cookbook 3rd, David Beazley and Brian Jones,
       O’Reilly Media, Inc.

    """
    __slots__ = ['name', '_seq', '_qual']

    def __init__(self, name, seq, qual=None):
        self.name = name
        self._qual = qual
        self.seq = seq

    @property
    def seq(self):
        return self._seq

    @seq.setter
    def seq(self, new_seq):
        if self._qual is None:
            self._seq = new_seq
        elif len(self._qual) == len(new_seq):
            self._seq = new_seq
        else:
            raise FormatError(
                'Seq', 'new sequence length mismatches')

    @property
    def qual(self):
        return self._qual

    @qual.setter
    def qual(self, new_qual):
        if len(self._seq) == len(new_qual):
            self._qual = new_qual
        else:
            raise FormatError(
                'Seq', 'new quality length mismatches')

    def __repr__(self):
        return "Seq(name={:s}, seq={:s}, qual={:s})".format(
            repr(self.name),
            repr(self.seq),
            repr(self.qual) if self.qual else "None"
        )
