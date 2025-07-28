import pandas as pd


def compare_csv_files(file1_path, file2_path):
    """
    Compares two CSV files for data differences.
    Returns: dict of differences.
    """
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    diff_rows = pd.concat([df1, df2]).drop_duplicates(keep=False)
    result = {
        'shape_file1': df1.shape,
        'shape_file2': df2.shape,
        'diff_rows': diff_rows
    }
    return result


# Example usage:
if __name__ == "__main__":
    result = compare_csv_files('source.csv', 'target.csv')
    print(f"Rows only in one file:\n{result['diff_rows']}")
