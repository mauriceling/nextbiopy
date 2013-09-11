from unittest import TestCase
from nose.tools import ok_, eq_, raises
import nextbiopy as nb

def test_core_class_lifted():
    ok_(nb.Seq is nb.core.Seq, "class Seq not lifted to module root")
    ok_(nb.FormatError is nb.core.FormatError,
        "exception FormatError not lifted to module root")


class TestCoreFormatError(TestCase):
    def test_simple_raise_formaterror(self):
        try:
            raise nb.FormatError()
        except nb.FormatError as e:
            ok_(e.format_type is None)
            ok_(e.msg is None)

    def test_formaterror_attr(self):
        try:
            raise nb.FormatError('class', 'you raise it yourself')
        except nb.FormatError as e:
            eq_(e.format_type, 'class')
            eq_(e.msg, 'you raise it yourself')
            eq_(repr(e), 'On handling type class, you raise it yourself')


class TestCoreClassSeqNoQual(TestCase):
    def setUp(self):
        self.expected_name = 'seq_id'
        self.expected_seq = 'ATCGTCGA'
        self.seq = nb.Seq(self.expected_name, self.expected_seq)

    def test_seq_attr_properly_set(self):
        eq_(self.seq.name, self.expected_name)
        eq_(self.seq.seq, self.expected_seq)

    def test_seq_quality_nullity(self):
        ok_(self.seq.qual is None)


class TestCoreClassSeqWithQual(TestCase):
    def setUp(self):
        self.expected_name = 'seq_id'
        self.expected_seq = 'ATCGTCGA'
        self.expected_qual = 'mmmmmmmm'
        self.seq = nb.Seq(
            self.expected_name,
            self.expected_seq,
            self.expected_qual
        )

    def test_seq_attr_quality_properly_set(self):
        eq_(self.seq.qual, self.expected_qual)

    @raises(nb.FormatError)
    def test_assign_inequal_quality_length_error(self):
        self.seq.qual = 'm' * 6

    @raises(nb.FormatError)
    def test_assign_inequal_quality_length_error(self):
        self.seq.seq = self.expected_seq[:6]

    @raises(nb.FormatError)
    def test_initial_inequal_length_error(self):
        nb.Seq(
            self.expected_name,
            self.expected_seq,
            self.expected_qual[:len(self.expected_seq) - 1]
        )
