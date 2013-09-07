"""Core data structure

.. moduleauthor:: Liang Bo Wang<ccwang002@gmail.com>

"""

class Seq():
    """Core class storing one sequence record.

    Attributes
    ----------
    _name : string
        Name of the sequence

    _seq : string
        Sequence

    _qual : string, optional
        Quality information (Default of is ``None``)

    """
    def __init__(self, name, seq, qual=None):
        self._name = name
        self._seq = seq
        self._qual = qual
