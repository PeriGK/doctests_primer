def addme(a):
    """
    This is a docstring. Please do not confuse it with doctests. They both mean to provide forms
    of documentation, but doctests are executable too
    >>> addme(4)
    8
    >>> addme('a')
    'aa'
    """
    return a + a

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(addme(1))