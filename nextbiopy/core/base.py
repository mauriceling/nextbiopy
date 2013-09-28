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
        return "On handling type {0.format_type}, {0.msg}".format(self)

class Seq():
    """Core class storing one sequence record.

    This class is the base class storing information about sequences.
    For example, a FASTA [1]_ file contains mutliple sequence record::

        >name of the sequence
        ATCGATCGATCGATCG
        >another sequence
        GCTAGCTAGCTA

    It contains 2 records of sequence. In fasta, each sequence record
    has a name and sequence itself.
    While for FASTQ [2]_ file, a seqeunce record has
    an additional information **quality**::

        @SEQ_ID
        GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
        +
        !''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65

    Nextbiopy internally store these seqeuence records using this class
    :class:`~!nextbiopy.Seq`

    Examples
    --------
    Creat a sequence instance is easy.

        >>> s = Seq('ATCG')
        >>> s
        Seq(name=None, seq='ATCG', qual=None)

    If ``name`` is not given, it will be set as ``None`` by default.

        >>> s.name
        None

    Quality information also is not required.
    One can add it later by setting the ``qual`` attribute.

        >>> s.qual = "!'*("
        >>> s
        Seq(name=None, seq='ATCG', qual="!'*(")

    All attributes, ``name``, ``seq`` and ``qual`` can be set explicitly
    at the same time.

        >>> s = Seq(name='myseq', seq='TT', qual='qq')

    For changing sequence and quality simultaneously, use
    :meth:`~nextbiopy.Seq.update`.

    An exception :exc:`~nextbiopy.FormatError`
    will be thrown if length of sequence and its quality are not the same.

        >>> s.qual = "!!"       # len(s.seq) is 4
        Traceback (most recent call last):
            ...
        FormatError: On handling type Seq, new quality length mismatches

    If quality is not given, changing sequence is simple by direct
    attribute access.

        >>> s = Seq('ATCG')
        >>> s.seq = 'ATCATA'


    Attributes
    ----------
    name : string, optional
        Name of the sequence

    seq : string
        Sequence

    qual : string, optional
        Quality information

    Raises
    ------
    FormatError
        If length of sequence and quality are not same.

    Notes
    -----
    By denoting ``__slots__``, user cannot add new attribute to
    instances. However, the memory use reduces. [3]_


    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/FASTA_format
    .. [2] http://en.wikipedia.org/wiki/FASTQ_format
    .. [3] Python Cookbook 3rd, David Beazley and Brian Jones,
           O’Reilly Media, Inc.
    """
    __slots__ = ['name', '_seq', '_qual']

    def __init__(self, seq, name=None, qual=None):
        self.name = name
        self.update(seq, qual)

    def update(self, new_seq, new_qual=None):
        """Modify both ``seq`` and ``qual`` together.

        Parameters
        ----------
        new_seq : string
        new_qual : string, optional

        Raises
        ------
        FormatError
            If length of sequence and quality are not same.

        Examples
        --------

            >>> s = Seq('ATA', '> <')
            >>> s.update('GCTA', '))((')
            >>> s
            Seq(name='myseq', seq='GCTA', qual="))((")

        """
        Seq._validate(new_seq, new_qual)
        self._seq = new_seq
        self._qual = new_qual

    @property
    def seq(self):
        return self._seq

    @seq.setter
    def seq(self, new_seq):
        if self._qual is None:
            self._seq = new_seq
        else:
            self.update(new_seq, self.qual)

    @property
    def qual(self):
        return self._qual

    @qual.setter
    def qual(self, new_qual):
        self.update(self.seq, new_qual)

    @classmethod
    def _validate(cls, new_seq, new_qual):
        if new_qual is not None and len(new_seq) != len(new_qual):
            raise FormatError(cls, 'seq and qual length mismatch')

    def __repr__(self):
        return (
            "Seq(name={0.name!r}, seq={0.seq!r}, qual={0.qual!r})".format(self)
        )
