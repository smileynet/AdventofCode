import utils

x = 0
y = 0

moves = utils.read_input_per_line('day_2_inputs')

# PART 1
for move in moves:
  direction, amount = move.split(' ')
  amount = int(amount)

  if direction == "forward":
    x += amount
  elif direction == "up":
    y -= amount
  elif direction == "down":
    y +=amount

outcome = x * y

print(f'part 1 outcome: {outcome}')

# PART 2
aim = 0
horizontal_pos = 0
depth = 0

for move in moves:
  direction, amount = move.split(' ')
  amount = int(amount)

  if direction == "forward":
    horizontal_pos += amount
    depth += aim * amount
  elif direction == "up":
    aim -= amount
  elif direction == "down":
    aim +=amount

outcome = horizontal_pos * depth

print(f'part 2 outcome: {outcome}')