def add(a, b):
    """
    Add two numbers
    :param a:
    :param b:
    :return: The sum of a and b
    """
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('')

    return a + b
