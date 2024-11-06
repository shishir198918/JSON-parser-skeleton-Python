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
    digit = {
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "-",
    }
    pos_digit = {
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    }
    non_rep = {"e", "E", "+", ".", "-"}
    if (
        input_string[0] == "."
        or input_string[0] == " "
        or input_string[:2] == "00"
        or (input_string[0] == "-" and input_string[1:3] == "00")
        or input_string[:2] == "--"
        or input_string[0] == "+"
        or (input_string[0] == "0" and input_string[1] in pos_digit)
        or (input_string[:2] == "-0" and input_string[2] in pos_digit)
    ):
        return None

    index = 0
    counter_point = True
    counter_exponent = True
    counter_sign = True
    if input_string[index] in digit and input_string[-1] not in non_rep:
        # print(input_string[index])
        index = index + 1
        # numbers = digit.union(non_rep)

        while index < len(input_string):
            # print(input_string[index])
            if input_string[index] in pos_digit:
                index = index + 1
            elif input_string[index] == "." and counter_point:
                counter_point = False
                index = index + 1
            elif (
                input_string[index] == "E" or input_string[index] == "e"
            ) and counter_exponent:
                counter_exponent = False
                index = index + 1
                if (
                    input_string[index] == "-" or input_string[index] == "+"
                ) and counter_sign:
                    counter_sign = False
                    index = index + 1
            else:
                break
        if input_string[:index] == "-":
            return None
        else:
            return float(input_string[:index]), input_string[index:]
    return None


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
