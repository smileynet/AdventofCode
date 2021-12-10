import utils

def get_bit_frequency(list_to_process):
  
  bits = []

  for i in range(0,len(readings[0])):
    bits.append({'ones':0, 'zeros':0})

  for item in list_to_process:
    for i in range(0,len(item)):
      if item[i] == "1":
        bits[i]['ones'] += 1
      elif item[i] == "0":
        bits[i]['zeros'] += 1

  return bits

def get_bit_pattern(bit_frequency, match_type):
  result = ''

  for bit in bit_frequency:
    if bit['ones'] > bit['zeros']:
      if match_type == "greater_than":
        result += '1'
      elif match_type == "less_than":
        result += '0'

    elif bit['ones'] < bit['zeros']:
      if match_type == "greater_than":
        result += '0'
      elif match_type == "less_than":
        result += '1'

    elif bit['ones'] == bit['zeros']:
      if match_type == "greater_than":
        result += '1'
      elif match_type == "less_than":
        result += '0'      

  return result

def common_match(list_to_match, match_type): 
  previous_results = list_to_match
  new_results = []
  bits = get_bit_frequency(previous_results)
  pattern_to_match = get_bit_pattern(bits,match_type)

  for bit in range(0,len(previous_results[0])):
    for result in previous_results:
      if result[bit] == pattern_to_match[bit]:
          new_results.append(result)

    if len(new_results) == 1:
      return new_results[0]
    else:
      previous_results = new_results
      new_results = []
      bits = get_bit_frequency(previous_results)
      pattern_to_match = get_bit_pattern(bits,match_type)

readings = utils.read_input_per_line('day_3_inputs')

## PART 1

bits = get_bit_frequency(readings)

gamma_rate = int(get_bit_pattern(bits,"greater_than"),2)
epsilon_rate = int(get_bit_pattern(bits,"less_than"),2)

print(f'gamma_rate: {gamma_rate}, epsilon_rate: {epsilon_rate}')

power_consumption = gamma_rate * epsilon_rate

print(f'power_consumption: {power_consumption}')

## PART 2

oxygen_rate = int(common_match(readings,"greater_than"),2)
c02_rate = int(common_match(readings,"less_than"),2)

print(f'oxygen_rate: {oxygen_rate}, c02_rate: {c02_rate}')

life_support_rating = oxygen_rate * c02_rate

print(f'life_support_rating: {life_support_rating}')
