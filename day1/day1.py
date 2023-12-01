from enum import Enum


def decode(input_array: [str]) -> int:
    total = 0
    for string in input_array:
        total += int(find_first_and_last_number(string))
    return total


def text_to_int(number: str) -> int:
    match number:
        case "zero":
            return "0"
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"


numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_first_and_last_number(input_string: str) -> str:
    first_num = None
    last_num = None
    count = 0
    input_string = input_string
    for character in input_string:
        if character.isdigit():
            if first_num is None:
                first_num = character
            last_num = character
        else:
            for number in numbers:
                if input_string[count:].find(number) == 0:
                    if first_num is None:
                        first_num = text_to_int(number)
                    last_num = text_to_int(number)
        count += 1

    return first_num + last_num


file = open("data.txt", "r", encoding="UTF8")
input_array = file.readlines()
file.close()

coordinates = decode(input_array)
print(coordinates)
