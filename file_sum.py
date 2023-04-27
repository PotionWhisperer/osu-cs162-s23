"""

Name: Juan A Wagner

GitHub ID: dota247 : https://github.com/dota247

Date: 04/27/2023

Description: Takes the numbers in a text file and sums them up.

"""



def convert_str_to_int(str_input):
    """
    Converts a string to an integer.
    """

    str_input = str_input.rstrip()

    try:
        int_output = int(str_input)
    except ValueError:
        try:
            int_output = int(float(str_input))
        except ValueError:
            raise ValueError(f"Cannot convert '{str_input}' to an integer")

    return int_output

def file_sum(list_of_numbers):
    """
    Calculates the sum of a list of numbers.

    """
    numbers_file = open(list_of_numbers, 'r+')
    list_of_numbers = numbers_file.read()
    list_of_numbers = list_of_numbers.split('\n')
    numbers_file.close()

    sum = 0
    for number in list_of_numbers:
        number = convert_str_to_int(number)
        sum += number
    return sum






