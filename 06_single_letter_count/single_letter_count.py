def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    return None \
        if len(word) <= 0 \
        or len(letter) \
        or not isinstance(word,str) <= 0 \
        else word().count(letter.tolower())