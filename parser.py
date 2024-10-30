def parse_null(input_string):

    if input_string[:4] == "null":
        return None, input_string[4:]
    """Parses null

    >>> parse_null("null rest")
    (None, " rest")

    >>> parse_null("something else")
    None

    """


def parse_bool(input_string):

    if input_string[:4] == "true":
        return True, input_string[4:]
    elif input_string[:5] == "false":
        return False, input_string[:5]
    """Parses boolean

    >>> parse_bool("true rest")
    (True, " rest")

    >>> parse_bool("something else")
    None

    """


def parse_number(input_string):
    digit = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "e", "E", "-", "+", "."}
    if input_string[:2] == "00" or input_string[1:3] == "00" or input_string[0] == " ":
        return input_string
    index = 1
    if input_string[0] != "+" and input_string[0] in digit:
        while index < len(input_string):
            if input_string[index] in digit:
                index = index + 1
            else:
                break

        try:
            return int(input_string[:index]), input_string[index:]
        except ValueError:
            return float(input_string[:index]), input_string[index:]
    else:
        input_string
    """Parses number

    >>> parse_number("123.456 rest")
    (123.456, " rest")

    >>> parse_number("something else")
    None

    """


def parse_string(input_string):
    """Parses string

    >>> parse_string('"abc" rest')
    ("abc", " rest")

    >>> parse_string("something else")
    None

    """
    pass


def parse_array(input_string):
    """Parses array

    >>> parse_array("[1, 2, 3] rest")
    ([1, 2, 3], " rest")

    >>> parse_array("something else")
    None

    """
    pass


def parse_object(input_string):
    """Parses object

    >>> parse_object('{"key": "value", "name": 1337} rest')
    ({"key": "value", "name": 1337}, " rest")

    >>> parse_object("something else")
    None

    """
    pass


def parse_json(input_string):
    """Parses json

    >>> parse_json('[{"my": "value"}, 2, "just string"]')
    [{"my": "value"}, 2, "just string"]

    >>> parse_json('[{"my": "value"}, 2, "just string"] fakjds;')
    Traceback (most recent call last):
        ...
    ValueError: Extra data
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
