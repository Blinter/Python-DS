def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return {c: str(num1).count(c) for c in str(num1)} == \
        {c: str(num2).count(c) for c in str(num2)}
