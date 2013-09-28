from nextbiopy import Seq

class Fasta():
    """Fasta file representataion."""
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

