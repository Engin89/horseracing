import pandas as pd

eng_dict = {'segrar': 'wins',
            'starter': 'starts',
            'proc': 'procent',
            'bankod': 'circuitcode',
            'bana': 'circuit',
            'avstand': 'distance',
            'systemnr': 'systemnumber',
            'rad': 'row',
            'beskr': 'description',
            'msegrar': 'mwins',
            'mstarter': 'mwins',
            'mproc': 'mprocent'
}


def read_table(path, columns,header=None, nrows=None, **kwargs):
    df = pd.read_csv(path,  header=header, sep='\t', nrows=nrows, encoding='latin-1',
                     error_bad_lines=False, na_values=['\\N'],
                     **kwargs)
    df.columns = columns
    return df