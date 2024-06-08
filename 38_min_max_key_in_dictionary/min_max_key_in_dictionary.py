def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    min_key = None
    max_key = None

    for key in d:
        if min_key is None or key < min_key:
            min_key = key
        if max_key is None or key > max_key:
            max_key = key

    return (min_key, max_key)