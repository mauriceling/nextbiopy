from unittest import TestCase
from nose.tools import ok_, eq_, raises, assert_raises
import nextbiopy as nb
from nextbiopy.io import Fasta
import os

TEST_FASTA = os.path.join(
    os.path.split(__file__)[0], 'test_default.fasta'
)

MULTILINE_FASTA = os.path.join(
    os.path.split(__file__)[0], 'test_multiline.fasta'
)


class TestFastaOpen(TestCase):
    def test_fasta_open(self):
        Fasta(TEST_FASTA)

    @raises(TypeError)
    def test_fasta_unsupported_mode(self):
        Fasta(TEST_FASTA, 'b')

    def test_fast_content_manager(self):
        with Fasta(TEST_FASTA):
            pass

class TestFastaRead(TestCase):
    def setUp(self):
        self.fa_list = [
            Fasta(TEST_FASTA, multiline=False),
            Fasta(MULTILINE_FASTA)
        ]

    def test_gen_seq(self):
        for fa in self.fa_list:
            for seq in fa:
                ok_(isinstance(seq, nb.Seq))

    def test_seq_content(self):
        for fa in self.fa_list:
            seq = next(fa)
            eq_(seq.name, 'seq1')
            eq_(seq.seq, 'ATCG' * 4)
            ok_(seq.qual is None)
            seq = next(fa)
            eq_(seq.name, 'seq2')
            eq_(seq.seq, 'GCTA' * 4)
            ok_(seq.qual is None)
            assert_raises(StopIteration, next, fa)

class TestFastaWrite(TestCase):
    def setUp(self):
        from tempfile import NamedTemporaryFile
        temp_fasta = NamedTemporaryFile()
        self.fa = Fasta(temp_fasta.name, 'w')

    @raises(NotImplementedError)
    def test_expect_implementation_error(self):
        for seq in self.fa:
            pass

class TestFastaAppend(TestCase):
    def setUp(self):
        from tempfile import NamedTemporaryFile
        self.temp_fasta = NamedTemporaryFile('w', delete=False)
        self.temp_fasta.write(open(TEST_FASTA).read())
        self.temp_fasta.close()
        self.fa = Fasta(self.temp_fasta.name, 'a')

    @raises(NotImplementedError)
    def test_expect_implementation_error(self):
        for seq in self.fa:
            pass

    def test_correct_content_append(self):
        with Fasta(self.temp_fasta.name) as read_fa:
            eq_(sum(1 for seq in read_fa), 2)

    def tearDown(self):
        os.remove(self.temp_fasta.name)

