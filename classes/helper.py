# Standard classes / libraries
import pandas as pd

def get_row_index(df_column: list, value: str) -> int:
    """ Returns the index of the value in the dataframe column.

    Parameters
    ----------
    df_column : list
        The column of a dataframe as a list.
    value : str
        The search value to look for in the dataframe column.
    """

    if value in df_column:
        return df_column.index(value)

def replace_nan(df_column: list) -> list:
    """ Replaces all "NaN" in an empty Table widget cell with an empty string.
    
    Parameters
    ----------
    df_column : list
        The column of a dataframe as a list.

    Return
    ----------
    df_column : list
    """

    for i in range(len(df_column)):
        if df_column[i] in ["nan"]:
            df_column[i] = ""
    return df_column