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

    def __str__(self):
        return "On handling type {:s}, {:s}".format(
            self.format_type, self.msg)

class Seq():
    """Core class storing one sequence record.

    This class is the base class storing information about sequences.
    For example, a FASTA file contains mutliple sequence record.

    .. code-block:: none

        >name of the sequence
        ATCGATCGATCGATCG
        >another sequence
        GCTAGCTAGCTA

    It contains 2 records of sequence. In fasta, each sequence record
    has a name and sequence itself. While for FASTQ file, a seqeunce record has
    an additional information **quality**.

    .. code-block:: none

        @SEQ_ID
        GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
        +
        !''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65

    Nextbiopy internally store these seqeuence records using this class
    :class:`~!nextbiopy.core.Seq`

    Examples
    --------
    Creat a sequence instance is easy.

        >>> s = Seq('name', 'ATCG')
        >>> s
        Seq(name='name', seq='ATCG', qual=None)

    Quality information is not required.
    One can add it later by setting the ``qual`` attribute.

        >>> s.qual = "!'*("
        >>> s
        Seq(name='name', seq='ATCG', qual="!'*(")

    All attributes, ``name``, ``seq`` and ``qual`` can be modified later
    the same way we access attributes of a class.

    An exception :exc:`~nextbiopy.core.FormatError`
    will be thrown if length of sequence and its quality are not the same.

        >>> s.qual = "!!"       # len(s.seq) is 4
        Traceback (most recent call last):
            ...
        FormatError: On handling type Seq, new quality length mismatches

    If you don't want to assign name for a sequence,
    passing ``name=''`` or ``name=None`` will do

        >>> Seq('', 'ATCG')
        Seq(name='', seq='ATCG', qual=None)
        >>> Seq(None, 'ATCG')
        Seq(name=None, seq='ATCG', qual=None)


    Attributes
    ----------
    name : string
        Name of the sequence

    seq : string
        Sequence

    qual : string, optional
        Quality information


    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/FASTA_format
    .. [2] http://en.wikipedia.org/wiki/FASTQ_format

    """
    __slots__ = ['name', '_seq', '_qual']

    def __init__(self, name, seq, qual=None):
        """ Create an instance of a sequence record.

        Parameters
        ----------
        name : string
        seq : string
        qual : string, optional

        Raises
        ------
        FormatError
            If length of sequence and quality are not same.

        Notes
        -----
        By denoting ``__slots__``, user cannot add new attribute to
        instances. However, the memory use reduces. [3]_

        .. [3] Python Cookbook 3rd, David Beazley and Brian Jones,
           O’Reilly Media, Inc.
        """
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
            repr(self.qual)
        )
