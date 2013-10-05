from unittest import TestCase
from nose.tools import ok_, eq_, raises, assert_raises
import nextbiopy as nb
from nextbiopy.io import Fastq
import os

TEST_FASTQ = os.path.join(
    os.path.split(__file__)[0], 'test_default.fastq'
)

MULTILINE_FASTQ = os.path.join(
    os.path.split(__file__)[0], 'test_multiline.fastq'
)

class TestFastqRead(TestCase):
    def setUp(self):
        self.fq_list = [
            Fastq(TEST_FASTQ, multiline=False),
            Fastq(MULTILINE_FASTQ)
        ]

    def test_seq_content(self):
        for fq in self.fq_list:
            seq = next(fq)
            eq_(seq.name, 'seq1')
            eq_(seq.seq, 'ATCG' * 4)
            eq_(seq.qual, '\(^  ^)/' * 2)
            seq = next(fq)
            eq_(seq.name, 'seq2')
            eq_(seq.seq, 'GCTA' * 4)
            eq_(seq.qual, '>///< $$$$ >///<')
            assert_raises(StopIteration, next, fq)
