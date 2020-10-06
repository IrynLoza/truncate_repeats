"""Truncate repeating characters into one character.

For example:

>>> truncate('aaaaabbbbbcccaaaa')
'abca'

>>> truncate('hi there')
'hi there'

The function should be able to handle special characters, punctuation, and/or
numbers:

>>> truncate('hi   !!! wooow')
'hi ! wow'
"""

def truncate(string):
    """Truncate repeating characters in a string."""
    result = ''

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            result+= string[i]
    result+= string[-1]

    return result       

        

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
