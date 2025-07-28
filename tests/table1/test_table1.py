import pytest
import pandas as pd
from src.data_validations import data_compare_check


def test_file_to_file(tmp_path):
    # Create small test CSVs
    df1 = pd.DataFrame({"id": [1, 2], "val": ["a", "b"]})
    df2 = pd.DataFrame({"id": [2, 3], "val": ["b", "c"]})
    f1 = tmp_path / "f1.csv"
    f2 = tmp_path / "f2.csv"
    df1.to_csv(f1, index=False)
    df2.to_csv(f2, index=False)

    result = data_compare_check.compare_file_to_file(str(f1), str(f2))
    # Expect row with id=1 and id=3 as differences
    assert set(result['diff_rows']['id']) == {1, 3}
