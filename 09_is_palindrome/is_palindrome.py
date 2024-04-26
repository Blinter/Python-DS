def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.replace(' ','').lower()
    i = 0
    while(i<len(phrase)):
        if(phrase[len(phrase)-i-1] != phrase[i]):
            return False
        #print(phrase[i] + " " + phrase[len(phrase)-i-1])
        i+=1;
    return True