def null_value_check(data, check_columns):
    """Return rows with nulls in the specified columns."""
    null_rows = []
    for row in data:
        for col in check_columns:
            if row[col] is None:
                null_rows.append(row)
                break
    return null_rows
