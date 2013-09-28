from nextbiopy import Seq

class Fasta():
    """Fasta file representataion.

    This class handles the I/O between FASTA file. Normally FASTA has two
    possible forms::

        >name of the sequence
        ATCGATCGATCGATCG
        >another sequence
        GCTAGCTAGCTA

    This type of FASTA is referred as **single line** FASTA, since for
    each record, sequence takes only one line (``\\n``).

    On the other hand, another type of FASTA is referred as **multiline**
    FASTA, which has the form::

        >name of the sequence
        ATCGATCGATCGATCGATCGATAGCATAT...
        TCGATATACGGGATACGAGACCAAATATT...
        ...
        ATATC
        >another sequence
        TCGAGATACGAGC...

    some record can have sequence spanning over multiple lines.

    Both types can be read by

        >>> fasta = Fasta('path/to/fasta')
        >>> next(fasta)
        Seq(name='name of the sequence', seq='ATCG...ATCG', qual=None)

    So the instance is *iterable* in **read** (``r``) mode,
    record will be return as :class:`~nextbiopy.Seq` instances.

    By default ``multiline`` is assumed. However, if it is a single line
    FASTA, the parsing speed will be **boosted** significantly.
    So if one knows how the FASTA file actually looks like
    (try ``head some.fasta`` for a quick look),
    it is always encouraged to set ``multiline=False``.

    Examples
    --------

    Reading a single line Fasta file on a for loop.

        >>> fasta = Fasta('path/to/single_line.fasta', multiline=False)
        >>> for seq in fasta:
        ...     pass

    Count number of total records.

        >>> sum(1 for seq in fasta)

    Combined with content manager

        >>> with Fasta('path/to/single_line.fasta', multiline=False) as fa:
        ...     for seq in fa:
        ...         pass

    Attributes
    ----------

    mode : {'r', 'w', 'a'}

        FASTA File mode, by default it reads an external fasta file. The
        meaning of mode is same as built-in :class:`file` mode, and is
        passed to it internally.

    multiline : True

    """
    def __init__(self, fasta_path, mode='r', multiline=True):
        self.multiline = multiline
        if mode not in ['r', 'w', 'a']:   # TODO:  ['w', 'a']
            raise TypeError("Unsupported mode type")
        self._file = open(fasta_path, mode)
        self._mode = mode
        if self._mode == 'r':
            self._seq_generator = self._gen_seq()
        elif mode == 'w':
            pass
        elif mode == 'a':
            pass

    def __enter__(self):
        return self

    def __exit__(self, exc_ty, exc_val, tb):
        pass

    def __iter__(self):
        if self._mode == 'r':
            return self._seq_generator
        else:
            raise NotImplementedError('Not in read mode')

    def __next__(self):
        return next(self._seq_generator)

    def _gen_seq(self):
        """Return generator of :class:`~nextbiopy.core.Seq` records"""
        if self.multiline:
            # if a record spans over two lines, then whether a record ends
            # depends on the initial letter of each line.
            seq_id = None
            seq_part = None
            for line in self._file:
                if line.startswith('>'):
                    if seq_id is not None:
                        yield Seq(name=seq_id, seq=''.join(seq_part))

                    seq_id = line[1:-1]
                    seq_part = []
                else:
                    seq_part.append(line[:-1])   # append the sequence
            if seq_id is not None:
                yield Seq(name=seq_id, seq=''.join(seq_part))

        else:
            # if it is a standard two-line-a-record fasta,
            # the parsing can speed up by no guessing about
            # whether a sequence is ended.
            for line_id, line_seq in zip(*[iter(self._file)] * 2):
                yield Seq(name=line_id[1:-1], seq=line_seq[:-1])

