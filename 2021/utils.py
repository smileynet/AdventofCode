# USAGE: data = read_input('day_1_inputs')
def read_input(file_name):
    file = open(file_name, "r")
    return file.read()


def read_input_per_line(file):
    with open(file) as my_file:
        data_array = my_file.readlines()
    return data_array
