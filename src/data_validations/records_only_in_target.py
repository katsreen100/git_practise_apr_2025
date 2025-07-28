import pandas as pd

def records_only_in_target(df_source, df_target):
    """
    Returns rows present only in df_target (not in df_source).
    """
    return pd.concat([df_target, df_source, df_source]).drop_duplicates(keep=False)
