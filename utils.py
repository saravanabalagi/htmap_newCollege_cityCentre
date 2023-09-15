import itertools
import pandas as pd


def list_minify(l: list, range_sep=':', list_sep=";"):
    list_of_lists = (list(x) for _, x in itertools.groupby(l, lambda x, c=itertools.count(): next(c)-x))
    return list_sep.join(range_sep.join(map(str, [l[0], l[-1]][:len(l)])) for l in list_of_lists)


def list_unminify(txt: str, flatten=False):
    l = []
    if pd.isna(txt): return l
    for r in txt.split(';'):
        e = [int(e) for e in r.split(':')]
        l_row = list(range(e[0], e[-1]+1))
        if flatten: 
            l.extend(l_row)
        else: 
            l.append(l_row)
    return l
