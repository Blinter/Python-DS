def product(a, b):
    """Return product of a and b.
        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """    
    return a*b if isinstance(a, int) and isinstance(b, int) else 0
