import pandas as pd

def records_only_in_source(df_source, df_target):
    """
    Returns rows present only in df_source (not in df_target).
    """
    return pd.concat([df_source, df_target, df_target]).drop_duplicates(keep=False)
