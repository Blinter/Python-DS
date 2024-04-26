def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    return \
        None if not isinstance(a, int) and not isinstance(b, int) \
        else 'Numbers are equal' if b==a \
        else 'Second is greater' if b>a \
        else 'First is greater'