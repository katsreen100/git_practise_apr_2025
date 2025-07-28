def schema_check(source_schema, target_schema):
    """Check if source and target schemas are identical (as lists of column names)."""
    return source_schema == target_schema
