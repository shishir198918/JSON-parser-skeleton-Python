def parse_null(input_string):
    """Parses null

    >>> parse_null("null rest")
    (None, " rest")

    >>> parse_null("something else")
    None


    """
    if input_string[:4] == "null":
        print("mukul2")
        return None, input_string[4:]
    else:
        print("Mukul1")
        return None


parse_null("something else")


def parse_bool(input_string):
    """Parses boolean

    >>> parse_bool("true rest")
    (True, " rest")

    >>> parse_bool("something else")
    None

    """
    if input_string[:4] == "true":
        return True, input_string[4:]
    elif input_string[:5] == "false":
        return False, input_string[:5]


def parse_number(input_string):
    """Parses number

    >>> parse_number("123.456 rest")
    (123.456, " rest")

    >>> parse_number("something else")
    None

    """
    index = 0
    if index < len(input_string) and input_string[index] == "-":
        index = index + 1
        if index < len(input_string) and input_string[index] == "0":
            index = index + 1
        elif index < len(input_string) and (input_string[index]).isdigit():
            while index < len(input_string) and (input_string[index]).isdigit():
                index = index + 1

    elif index < len(input_string) and (input_string[index]).isdigit():
        while index < len(input_string) and (input_string[index]).isdigit():
            index = index + 1

    elif index < len(input_string) and input_string[index] == "0":
        index = index + 1

    else:
        return None
    # if index==len(input_string):
    # return float(input_string[:index])

    if index < len(input_string) and input_string[index] == ".":
        index = index + 1
        while index < len(input_string) and ((input_string[index]).isdigit()):
            index = index + 1

    elif index < len(input_string) and (
        input_string[index] == "E" or input_string[index] == "e"
    ):

        index = index + 1
        if (
            index < len(input_string)
            and input_string[index] == "+"
            or input_string[index] == "-"
        ):
            index = index + 1
            if index < len(input_string) and input_string[index].isdigit():
                while index < len(input_string) and (input_string[index]).isdigit():
                    index = index + 1
            else:
                return None

        elif index < len(input_string) and input_string[index].isdigit():
            while index < len(input_string) and (input_string[index]).isdigit():
                index = index + 1
        else:
            return None
    if input_string[:index] == "-":
        return None
    return float(input_string[:index]), input_string[index:]

def parse_string(input_string):
    """Parses string

    >>> parse_string('"abc" rest')
    ("abc", " rest")

    >>> parse_string("something else")
    None

    """
    def four_step(index, input_string):
    if input_string[index]=="u":
        pass


def one_step(index, input_string):
    charc = {"b": "\b", '"': '"', "f": "\f", "n": "\n", "r": "\r", "t": "\t"}
    if input_string[index] in charc.keys():
        # print(len(input_string[index - 1] + input_string[index]))
        return charc[input_string[index]]
    else:
        pass


def string_parser(input_string):
    output_string = ""
    index = 1
    if input_string[0] == '"' and input_string[-1] == '"':
        while index < len(input_string[1:-1]):
            if input_string[index] == "\\":
                output_string = output_string[:index] + one_step(
                    index + 1, input_string
                )
                index = index + 2
            else:
                output_string = output_string + input_string[index]
                index = index + 1
        return output_string
    else:
        return None


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
