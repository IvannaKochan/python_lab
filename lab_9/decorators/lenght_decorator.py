"""
length decorator
"""
def length_decorator(func):
    """

    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            length = len(result)
            print("Length:", length)
        except TypeError:
            print("Length: 1")
        return result

    return wrapper
