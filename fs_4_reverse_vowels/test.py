def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    # Convert the string to a list for easier manipulation
    s_list = list(s)
    # Initialize pointers for the start and end of the string
    start, end = 0, len(s_list) - 1

    while start < end:
        # Move start pointer to the next vowel
        while start < end and s_list[start] not in vowels:
            start += 1
        # Move end pointer to the previous vowel
        while start < end and s_list[end] not in vowels:
            end -= 1
        # Swap the vowels
        s_list[start], s_list[end] = s_list[end], s_list[start]
        # Move pointers inward
        start += 1
        end -= 1

    # Convert the list back to a string
    return ''.join(s_list)