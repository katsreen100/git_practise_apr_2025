def print_compare_result(result):
    print("Source shape:", result.get('shape_file') or result.get('shape_source_table'))
    print("Target shape:", result.get('shape_file2') or result.get('shape_table') or result.get('shape_target_table'))
    print("Rows different:")
    print(result['diff_rows'].head())   # Show top rows only
