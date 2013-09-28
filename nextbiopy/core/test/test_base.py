from unittest import TestCase
from nose.tools import ok_, eq_, raises
import nextbiopy as nb

def test_core_class_lifted():
    ok_(nb.Seq is nb.core.base.Seq, "class Seq not lifted to module root")
    ok_(nb.FormatError is nb.core.base.FormatError,
        "exception FormatError not lifted to module root")


class TestFormatError(TestCase):
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
            eq_(str(e), 'On handling type class, you raise it yourself')


class TestClassSeqSimple(TestCase):
    def setUp(self):
        self.expected_seq = 'ATCGTCGA'
        self.seq = nb.Seq(self.expected_seq)

    def test_seq_properly_set(self):
        eq_(self.seq.seq, self.expected_seq)

    def test_seq_name_nullity(self):
        ok_(self.seq.name is None)

    def test_seq_qual_nullity(self):
        ok_(self.seq.qual is None)


class TestClassSeqNoQual(TestCase):
    def setUp(self):
        self.expected_name = 'seq_id'
        self.expected_seq = 'ATCGTCGA'
        self.new_seq = 'ATCG'
        self.seq = nb.Seq(self.expected_seq, name=self.expected_name)

    def test_change_sequence(self):
        self.seq.seq = self.new_seq
        eq_(self.seq.seq, self.new_seq)

    def test_change_sequence_using_update(self):
        self.seq.update(self.new_seq, None)
        eq_(self.seq.seq, self.new_seq)
        ok_(self.seq.qual is None)

    def test_seq_attr_properly_set(self):
        eq_(self.seq.name, self.expected_name)
        eq_(self.seq.seq, self.expected_seq)

    def test_seq_quality_nullity(self):
        ok_(self.seq.qual is None)


class TestClassSeqWithQual(TestCase):
    def setUp(self):
        self.expected_name = 'seq_id'
        self.expected_seq = 'ATCGTCGA'
        self.expected_qual = 'mmmmmmmm'
        self.seq = nb.Seq(
            self.expected_seq,
            self.expected_name,
            self.expected_qual
        )

    def test_repr_format(self):
        eq_(repr(self.seq),
            "Seq(name='seq_id', seq='ATCGTCGA', qual='mmmmmmmm')")

    def test_seq_attr_quality_properly_set(self):
        eq_(self.seq.qual, self.expected_qual)

    def test_change_quality(self):
        new_qual = '(' * 8
        self.seq.qual = new_qual
        eq_(self.seq.qual, new_qual)

    def test_update(self):
        new_seq = 'ATCG'
        new_qual = '))(('
        self.seq.update(new_seq, new_qual)
        eq_(self.seq.seq, new_seq)
        eq_(self.seq.qual, new_qual)

    @raises(nb.FormatError)
    def test_assign_inequal_quality_length_error(self):
        self.seq.qual = 'm' * 6

    @raises(nb.FormatError)
    def test_assign_inequal_seq_length_error(self):
        self.seq.seq = self.expected_seq[:6]

    @raises(nb.FormatError)
    def test_initial_inequal_length_error(self):
        nb.Seq(
            self.expected_name,
            self.expected_seq,
            self.expected_qual[:len(self.expected_seq) - 1]
        )
