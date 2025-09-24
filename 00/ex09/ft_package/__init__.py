def count_in_list(lst: list, item) -> int:
    """Counts the number of occurrences of an item in a list."""
    if not isinstance(lst, list):
        print("Error: The first argument must be a list.")
        return 0
    return lst.count(item)
