def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False

        >>> list_check([[1], "nope", 1])
        False

        >>> list_check([[1], [2, 3], [4, 5]])
        True
    """
    return all(False for d in [c for c in lst if not isinstance(c, list)])
