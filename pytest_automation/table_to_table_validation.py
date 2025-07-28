import pandas as pd
from sqlalchemy import create_engine


def compare_tables(conn_str, source_table, target_table):
    """
    Compares two database tables.
    Returns dict of differences.
    """
    engine = create_engine(conn_str)
    df1 = pd.read_sql_table(source_table, engine)
    df2 = pd.read_sql_table(target_table, engine)

    diff_rows = pd.concat([df1, df2]).drop_duplicates(keep=False)
    result = {
        'shape_source_table': df1.shape,
        'shape_target_table': df2.shape,
        'diff_rows': diff_rows
    }
    return result

# Example usage:
# result = compare_tables("sqlite:///mydb.sqlite", "table1", "table2")
