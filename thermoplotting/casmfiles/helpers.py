import pandas as pd

def pandas_from_casm_csv(filename):
    """Read a csv from a space separated file generated by casm,
    which has an annoying "#" in the header, causing pandas
    to insert an extra column of nonsense, and shifting all the values

    :filename: str
    :returns: pd DataFrame

    """
    dump=pd.read_csv(filename, delim_whitespace=True)

    returnable=dump[dump.columns[:-1]]
    returnable.columns=dump.columns[1:]

    return returnable
