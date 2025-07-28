def duplicate_check(data, key_columns):
    """Find duplicates based on key_columns."""
    seen = set()
    duplicates = []
    for row in data:
        key = tuple(row[col] for col in key_columns)
        if key in seen:
            duplicates.append(row)
        else:
            seen.add(key)
    return duplicates
