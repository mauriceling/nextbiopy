from nextbiopy import Seq
from nextbiopy.compat import PY2

def read_fasta(file_path, multiline=True):
    """FASTA parser returns generator of :class:`~nextbiopy.Seq` records.

    Parameters
    ----------
    file_path : string
        path to the FASTA file, passed to :func:`open()` internally

    multiline : bool, True
        whether a sequence record can span over multiple lines

    Examples
    --------

        >>> gen_seq = read_fasta('/path/to/your.fasta', multiline=False)
        >>> for seq in gen_seq:
        ...     print(seq)

    """
    with open(file_path, 'r') as fa:
        if multiline:
            # if a record spans over two lines, then whether a record ends
            # depends on the initial letter of each line.
            seq_id = None
            seq_part = None
            for line in fa:
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
            for line_id, line_seq in zip(*[iter(fa)] * 2):
                yield Seq(name=line_id[1:-1], seq=line_seq[:-1])

def read_fastq(file_path, multiline=True):
    """FASTQ parser returns generator of :class:`~nextbiopy.Seq` records.

    Parameters
    ----------
    file_path : string
        path to the FASTA file, passed to :func:`open()` internally

    multiline : bool, True
        whether a sequence record can span over multiple lines

    Examples
    --------

        >>> gen_seq = read_fastq('/path/to/your.fastq', multiline=False)
        >>> for seq in gen_seq:
        ...     print(len(seq.qual))

    """
    with open(file_path, 'r') as fq:
        if multiline:
            seq_id = None
            seq_part = None
            qual_part = None
            state = 'i'  # i: initial, s: seq, q: quality
            for line in fq:
                if line.startswith('@'):
                    if state == 'i':
                        pass  # first run
                    elif state == 'q':
                        seq = ''.join(seq_part)
                        qual = ''.join(qual_part)
                        if len(qual) < len(seq):
                            # a quality starts with @
                            qual_part.append(line[:-1])
                            continue
                        else:
                            yield Seq(
                                name=seq_id,
                                seq=seq,
                                qual=qual
                            )
                    seq_id = line[1:-1]
                    seq_part = []
                    qual_part = []
                    state = 's'
                elif line.startswith('+'):
                    state = 'q'
                    continue
                elif state == 's':
                    seq_part.append(line[:-1])
                else:
                    qual_part.append(line[:-1])

            yield Seq(
                name=seq_id,
                seq=''.join(seq_part),
                qual=''.join(qual_part)
            )
        else:
            for line_id, line_seq, _, line_qual in zip(*[iter(fq)] * 4):
                yield Seq(name=line_id[1:-1],
                          seq=line_seq[:-1],
                          qual=line_qual[:-1])


class Fasta:
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
    def __init__(self, file_path, mode='r', multiline=True):
        self.multiline = multiline
        self.file_path = file_path
        if mode not in ['r', 'w', 'a']:   # TODO:  ['w', 'a']
            raise TypeError("Unsupported mode type")
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

    def next(self):
        return self.__next__()

    def _gen_seq(self):
        if PY2:
            for s in read_fasta(self.file_path, self.multiline):
                yield s
        else:
            yield from read_fasta(self.file_path, self.multiline)

class Fastq(Fasta):
    """FASTQ file representation

    All operations are similar to :class:`~nextbiopy.io.Fasta`, but the file
    format is slightly different::

        @name of the sequence
        ATCGATCGATCGATC
        +
        \QAQ/\QAQ/\QAQ/
        @another sequence
        GCTAGCTAGCTA
        +
        !!(> <)!!QAQ

    Fastq can be also stored in multiline manner.

    Examples
    --------

    Same usage as :class:`~nextbiopy.io.Fasta`.

    Attributes
    ----------

    mode : {'r', 'w', 'a'}
    multiline : True

    """
    def _gen_seq(self):
        if PY2:
            for s in read_fastq(self.file_path, self.multiline):
                yield s
        else:
            yield from read_fastq(self.file_path, self.multiline)
