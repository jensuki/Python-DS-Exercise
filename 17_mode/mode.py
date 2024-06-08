def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    dictionary = {}

    for num in nums:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1

    max_count = 0
    mode = None

    for num, occurences in dictionary.items():
        if occurences > max_count:
            max_count = occurences
            mode = num

    return mode
