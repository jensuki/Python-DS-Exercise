def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    result = []
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            result.append(letter.upper())
        elif letter == to_swap.upper():
            result.append(letter.lower())
        else:
            result.append(letter)

    return ''.join(result)
