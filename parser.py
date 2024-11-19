import os


def parse_null(input_string):
    """parse_null

    >>> parse_null('null rest')
    (None, ' rest')

    >>> parse_null('something else') is None
    True
    """
    if input_string[:4] == "null":
        return None, input_string[4:]


def parse_bool(input_string):
    """parse_bool

    >>> parse_bool('true rest')
    (True, ' rest')

    >>> parse_bool('something else') is None
    True
    """
    if input_string[:4] == "true":
        return True, input_string[4:]
    elif input_string[:5] == "false":
        return False, input_string[5:]


def parse_number(input_string):
    """parse_number

    >>> parse_number('123.456 rest')
    (123.456, ' rest')

    >>> parse_number('something else') is None
    True
    """

    index = 0
    if index < len(input_string) and input_string[index] == "-":
        index = index + 1
        if index < len(input_string) and input_string[index] == "0":
            index = index + 1
        elif index < len(input_string) and (
            (input_string[index]).isdigit() and input_string[index] != "0"
        ):
            while index < len(input_string) and (input_string[index]).isdigit():
                index = index + 1

    elif index < len(input_string) and (
        (input_string[index]).isdigit() and input_string[index] != "0"
    ):
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

    if index < len(input_string) and (
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


def four_step(index, input_string):
    if input_string[index] == "u":
        pass


def one_step(index, input_string):
    charc = {"b": "\b", '"': '"', "f": "\f", "n": "\n", "r": "\r", "t": "\t"}
    if input_string[index] in charc.keys():
        # print(len(input_string[index - 1] + input_string[index]))
        return charc[input_string[index]]
    else:
        pass


def parse_string(input_string):
    """parse_string

    >>> parse_string('"abc" rest')
    ('abc', ' rest')

    >>> parse_string('something else') is None
    True
    """

    output_string = ""
    index = 1
    if input_string[0] == '"':

        while index < len(input_string) and input_string[index] != '"':
            if input_string[index] == "\\" and input_string[index + 1] == "u":
                index = index + 5

            if input_string[index] == "\\":
                output_string = output_string[:index] + one_step(
                    index + 1, input_string
                )
                index = index + 2
            else:
                output_string = output_string + input_string[index]
                index = index + 1

        return output_string, input_string[index + 1 :]
    else:
        return None


def whitespace_parse(input_string):
    whitespace = " \t\n\r"
    start_index = 0
    end_index = len(input_string)
    while start_index < end_index and input_string[start_index] in whitespace:
        start_index = start_index + 1
    while start_index < end_index and input_string[end_index - 1] in whitespace:
        end_index = end_index - 1
    return input_string[start_index:end_index]


def value(input_string):
    input_string = whitespace_parse(input_string)
    a = parse_null(input_string)
    if a:
        return a
    b = parse_bool(input_string)
    if b:
        return b
    c = parse_number(input_string)
    if c:
        return c
    d = parse_string(input_string)
    if d:
        return d
    e = parse_array(input_string)
    if e:
        return e
    e = parse_object(input_string)
    if e:
        return e


def parse_array(input_string):
    """Parses array

    >>> parse_array('[1, 2, 3] rest')
    ([1.0, 2.0, 3.0], ' rest')
    >>> parse_array('[1,"Shishir"') is None
    True
    >>> parse_array('[1,2,[1,2,3],4]')
    ([1.0, 2.0, [1.0, 2.0, 3.0], 4.0], '')

    >>> parse_array('[1,-2,3,4,[02,3,4]]') is None
    True

    >>> parse_array('something else') is None
    True
    """
    input_string = whitespace_parse(input_string)
    if input_string[0] != "[":
        return None
    l1_list = []

    if whitespace_parse(input_string[1:]) == "]":

        return l1_list, input_string[2:]
    check = value(input_string[1:])
    while check and (
        whitespace_parse(check[1])[0] == "," or whitespace_parse(check[1])[0] == "]"
    ):
        l1_list.append(check[0])
        # print(l1_list, check[1])
        if whitespace_parse(check[1])[0] == "]":
            return l1_list, check[1][1:]
        check = value(check[1][1:])
        # for checking if value rest of string return ""
        if check:
            if check[1]:
                continue
            else:
                break
        else:
            break


def key_value_parser(input_string):
    input_string = whitespace_parse(input_string)
    string = parse_string(input_string)

    if string:
        # check for rest string is not null
        if string[1]:

            rest = whitespace_parse(string[1])

            if rest[0] == ":":
                entry = value((rest[1:]))
                if entry:
                    return string[0], entry


def parse_object(input_string):
    """Parses object

    >>> parse_object('{"key": "value", "name": 1337} rest')
    ({'key': 'value', 'name': 1337.0}, ' rest')

    >>> parse_object('{"shishir":[78,89,90],   "pandey":[89,90,91],"a":{"sd":[1,"shi"]}},shisir}')
    ({'shishir': [78.0, 89.0, 90.0], 'pandey': [89.0, 90.0, 91.0], 'a': {'sd': [1.0, 'shi']}}, ',shisir}')

    >>> parse_object("something else") is None
    True
    """
    input_string = whitespace_parse(input_string)
    if input_string[0] != "{":
        return None
    d1_dict = {}

    if whitespace_parse(input_string[1:]) == "}":
        return d1_dict, input_string[2:]
    check = key_value_parser(input_string[1:])

    while check and (
        whitespace_parse(check[1][1])[0] == ","
        or whitespace_parse(check[1][1])[0] == "}"
    ):
        # print(check)
        d1_dict[check[0]] = check[1][0]
        # print(check[1][1])
        if whitespace_parse(check[1][1])[0] == "}":
            return d1_dict, check[1][1][1:]
        check = key_value_parser(check[1][1][1:])
        # print(check)
        if check:
            if check[1][1]:
                continue
            else:
                break
        else:
            break


def parse_json(input_string):
    """Parses json

    >>> parse_json('[{"my": "value"}, 2, "just string"]')
    [{'my': 'value'}, 2.0, 'just string']

    >>> parse_json('[{"my": "value"}, 2, "just string"] fakjds;')
    Traceback (most recent call last):
        ...
    Exception: Substring not in Json format
    """
    check = value(input_string)
    if check:
        if check[1]:
            raise Exception("Substring not in Json format")
        return check[0]
    else:
        raise Exception("Provide the correct Json format ")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    path = "c:\\Users\\Shiment\\Documents\\Bit-by-bit\\JSON-parser-skeleton-Python\\JSON File\\reddit.json"
    file = open(path, "r")
    string = file.read()
    print(parse_json(string))
