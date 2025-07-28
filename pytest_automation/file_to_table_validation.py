import pandas as pd
from sqlalchemy import create_engine


# pip install sqlalchemy

def compare_file_to_table(file_path, conn_str, table_name):
    """
    Compares a CSV file to a database table.
    Returns: dict of differences.
    """
    df_file = pd.read_csv(file_path)
    engine = create_engine(conn_str)
    df_table = pd.read_sql_table(table_name, engine)

    diff_rows = pd.concat([df_file, df_table]).drop_duplicates(keep=False)
    result = {
        'shape_file': df_file.shape,
        'shape_table': df_table.shape,
        'diff_rows': diff_rows
    }
    return result

# Example usage:
# result = compare_file_to_table("source.csv", "sqlite:///mydb.sqlite", "mytable")
