def whitespace_parse(input_string):
    whitespace = " \t\n\r"
    start_index = 0
    end_index = len(input_string)
    while start_index < end_index and input_string[start_index] in whitespace:
        start_index = start_index + 1
    while start_index < end_index and input_string[end_index - 1] in whitespace:
        end_index = end_index - 1
    return input_string[start_index:end_index]


def parse_number(input_string):
    input_string = whitespace_parse(input_string)

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
    charc = {
        "b": "\b",
        '"': '"',
        "f": "\f",
        "n": "\n",
        "r": "\r",
        "t": "\t",
        "/": "/",
        "\\": "\\",
    }
    if input_string[index] in charc.keys():
        # print(input_string[index])

        return charc[input_string[index]]
    else:
        pass


def parse_string(input_string):
    try:

        input_string = whitespace_parse(input_string)
        if input_string[0] != '"':
            return None
        output_string = ""
        # print(whitespace_parse(input_string[1:]))
        if whitespace_parse(input_string[1:]) == '"':

            return output_string, input_string[1:]
        index = 1
        lenght = len(input_string)
        # print(lenght)
        while index < lenght and input_string[index] != '"':

            if input_string[index] == "\\":
                if input_string[index + 1] == "u":
                    # print(index,input_string[index])
                    index = index + 5

            if input_string[index] == "\\":
                output_string = output_string[:index] + one_step(
                    index + 1, input_string
                )
                index = index + 2

            else:
                # print(index)
                output_string = output_string + input_string[index]
                index = index + 1

        if input_string[index] == '"':
            return output_string, input_string[index + 1 :]
    except UnicodeDecodeError:
        print("'charmap' codec can't decode byte 0x8f")
        # error_string = ""
        # error_string = "," + input_string[index + 1 :]
        # return output_string,error_string


def parse_null(input_string):

    input_string = whitespace_parse(input_string)
    if (
        input_string[:4] == "null"
        or input_string[:4] == "Null"
        or input_string[:4] == "NULL"
    ):
        # print(None, input_string[4:])
        return None, input_string[4:]


def parse_bool(input_string):
    input_string = whitespace_parse(input_string)
    if input_string[:4] == "true":
        print(True, input_string[4:])
        return True, input_string[4:]
    elif input_string[:5] == "false":
        print(False, input_string[5:])
        return False, input_string[5:]


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
    f = parse_object(input_string)
    if f:
        return f


def parse_array(input_string):

    input_string = whitespace_parse(input_string)
    if input_string[0] != "[":
        return None
    l1_list = []

    substring = whitespace_parse(input_string[1:])

    if substring[0] == "]":

        return l1_list, substring[1:]

    check = value(substring)

    while check and (
        whitespace_parse(check[1])[0] == "," or whitespace_parse(check[1])[0] == "]"
    ):
        l1_list.append(check[0])
        # print(l1_list, check[1])
        substring = whitespace_parse(check[1])
        if substring[0] == "]":
            return l1_list, substring[1:]
        check = value(substring[1:])
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
    # print(input_string)
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
    input_string = whitespace_parse(input_string)

    # print(input_string[1])

    if input_string[0] != "{":
        return None
    d1_dict = {}
    subString = whitespace_parse(input_string[1:])
    if subString[0] == "}":
        return d1_dict, subString[1:]
    check = key_value_parser(subString)

    # print(subString)

    while check and (
        whitespace_parse(check[1][1])[0] == ","
        or whitespace_parse(check[1][1])[0] == "}"
    ):

        d1_dict[check[0]] = check[1][0]
        # print(check[1][1])
        subString = whitespace_parse(check[1][1])
        if subString[0] == "}":

            return d1_dict, subString[1:]
        check = key_value_parser(subString[1:])
        # print(check)
        if check:
            if check[1][1]:
                continue
            else:
                break
        else:
            break


def parse_json(input_string):
    check = value(input_string)
    if check:
        if check[1]:
            raise Exception("Substring not in Json format")
        return check[0]
    else:
        raise Exception("Provide the correct Json format ")


import os


def test_case():

    root = "c:\\Users\\Shiment\\Documents\\Bit-by-bit\\JSON-parser-skeleton-Python\\JSON_file\\none_test_cases"

    file_list = os.listdir(root)
    for file in file_list[2:]:

        reply = input("Go ahead?: ").strip()
        if reply == "Y":
            path = os.path.join(root, file)
            file_name = open(path, "r", encoding="utf8")
            #     # print(">>>>>>>>")
            #     # print(file_name)
            file_read = file_name.read()
            print(value(file_read), file)
            file_name.close()
        else:
            print("Break")
            break


root = "c:\\Users\\Shiment\\Documents\\Bit-by-bit\\JSON-parser-skeleton-Python\\JSON_file\\reddit.json"
file_name = open(root, "r", encoding="utf8")
file_read = file_name.read()
print(parse_json(file_read))
file_name.close()
