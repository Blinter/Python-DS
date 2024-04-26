def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return ''.join([c.upper() if i == 0 else c for i, c in enumerate(phrase)])
    #return phrase[0].upper() + phrase[1::] if phrase else 