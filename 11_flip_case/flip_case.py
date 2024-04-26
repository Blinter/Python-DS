def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    return ''.join([
    i.upper() if i.lower() == to_swap.lower() and i.islower() else \
    i.lower() if i.lower() == to_swap.lower() and i.isupper() else \
    i for i in phrase])
"""
    backtrack solution
    returnstr = ""
    for i in phrase:
        if(to_swap.lower() == i.lower()):
            if i.islower():
                returnstr+=i.upper()
            else:
                returnstr+=i.lower()
        else:
            returnstr+=i
    return returnstr
"""