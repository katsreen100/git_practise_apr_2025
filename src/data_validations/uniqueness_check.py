def uniqueness_check(data, key_columns):
    """Check if rows are unique based on key_columns."""
    seen = set()
    for row in data:
        key = tuple(row[col] for col in key_columns)
        if key in seen:
            return False
        seen.add(key)
    return True
