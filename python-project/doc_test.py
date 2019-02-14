def square(x):
    """Returns the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """
    return ""


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


if __name__ == "__main__":
    import doctest
    t = doctest.testmod()
    if t.failed:
        fail()
    else:
        success()
