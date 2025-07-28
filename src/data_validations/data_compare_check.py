import pandas as pd
from sqlalchemy import create_engine

def compare_file_to_file(file1_path, file2_path):
    """
    Compare two CSV (or Excel) files for row-level differences.
    Returns: dict with shapes and differing rows.
    """
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)
    diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
    return {
        'shape_file1': df1.shape,
        'shape_file2': df2.shape,
        'diff_rows': diff
    }

def compare_file_to_table(file_path, conn_str, table_name):
    """
    Compare a CSV file to a database table.
    Returns: dict with shapes and differing rows.
    """
    df_file = pd.read_csv(file_path)
    engine = create_engine(conn_str)
    df_table = pd.read_sql_table(table_name, engine)
    diff = pd.concat([df_file, df_table]).drop_duplicates(keep=False)
    return {
        'shape_file': df_file.shape,
        'shape_table': df_table.shape,
        'diff_rows': diff
    }

def compare_table_to_table(conn_str, source_table, target_table):
    """
    Compare two database tables.
    Returns: dict with shapes and differing rows.
    """
    engine = create_engine(conn_str)
    df_src = pd.read_sql_table(source_table, engine)
    df_tgt = pd.read_sql_table(target_table, engine)
    diff = pd.concat([df_src, df_tgt]).drop_duplicates(keep=False)
    return {
        'shape_source_table': df_src.shape,
        'shape_target_table': df_tgt.shape,
        'diff_rows': diff
    }
