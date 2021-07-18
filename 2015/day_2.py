def get_paper_needed(length, width, height):
    side_a = length * width
    side_b = width * height
    side_c = height * length

    shortest_side = side_a
    if shortest_side > side_b:
        shortest_side = side_b
    if shortest_side > side_c:
        shortest_side = side_c

    area = 2 * side_a + 2 * side_b + 2 * side_c
    paper_needed = area + shortest_side
    return paper_needed


def get_ribbon_needed(length, width, height):
    side_a = length
    side_b = width
    side_c = height

    shortest_side = side_a
    second_shortest_side = 0
    if shortest_side > side_b:
        second_shortest_side = shortest_side
        shortest_side = side_b
    else:
        second_shortest_side = side_b
    if shortest_side > side_c:
        second_shortest_side = shortest_side
        shortest_side = side_c
    else:
        if second_shortest_side > side_c:
            second_shortest_side = side_c

    volume = length * width * height
    shortest_sides = 2 * shortest_side + 2 * second_shortest_side
    ribbon_needed = volume + shortest_sides
    return ribbon_needed


def read_input(file):
    with open(file) as my_file:
        data_array = my_file.readlines()
    return data_array


data = read_input('day_2_inputs')
total_paper_needed = 0
total_ribbon_needed = 0

for package in data:
    cleaned_package = package.strip('\n')
    length, width, height = cleaned_package.split('x')
    total_paper_needed += get_paper_needed(int(length), int(width), int(height))
    total_ribbon_needed += get_ribbon_needed(int(length), int(width), int(height))

print(f'Paper needed: {total_paper_needed}')
print(f'Ribbon needed: {total_ribbon_needed}')
