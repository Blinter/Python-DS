def reverse_vowels(s):
    words = s
    final = ''
    vowels = [(c, i) for i, c in enumerate(words) if c.lower() in 'aeiou']
    indexes = []
    vowels2 = []
    for c in vowels:
        vowels2.append(c[0])
        indexes.append(c[1])
    iii = 0
    temp_vowels = list(reversed(indexes))
    vowels_dict = dict()
    while iii < len(temp_vowels):
        vowels_dict[temp_vowels[iii]] = vowels2[iii]
        iii += 1
    iii = 0
    while iii < len(words):
        for (i, c) in vowels_dict.items():
            if i == iii:
                final += c
                break
        if len(final) != iii+1:
            final += words[iii]
        iii += 1
    return final
