import utils

reports = utils.read_input_per_line('day_1_inputs')

# PART 1
count = 0
for i in range(1, len(reports)):
    if int(reports[i - 1]) < int(reports[i]):
        count += 1

print(count)

# PART 2
count = 0
for i in range(3, len(reports)):
    window_a = (int(reports[i - 3]) + int(reports[i - 2]) + int(reports[i - 1])) / 3
    window_b = (int(reports[i - 2]) + int(reports[i - 1]) + int(reports[i])) / 3
    
    if window_a < window_b:
        count += 1

print(count)