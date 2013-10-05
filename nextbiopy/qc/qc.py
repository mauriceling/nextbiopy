import pandas as pd
import matplotlib.pyplot as plt
from nextbiopy.qc.parser import *

def base_qual(fpath):
    seq_record = to_df(read_seq(fpath))
    qual = seq_record['qual'].apply(lambda s: pd.Series(list(map(lambda c: ord(c) - 33, s))))
    ax = qual.boxplot(grid=False)
    plt.draw_if_interactive()
    return ax
