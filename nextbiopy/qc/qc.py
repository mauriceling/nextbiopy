import pandas as pd
from nextbiopy.qc.parser import *

def base_qual(fpath):
    seq_record = to_df(read_seq(fpath))
    qual = seq_record['qual'].apply(lambda s: pd.Series(list(map(lambda c: ord(c) - 33, s))))
    return qual.boxplot()
