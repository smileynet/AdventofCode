import utils

class CoordinateTracker:

    def __init__(self):
        self.coords = []
        self.current_x = 0
        self.current_y = 0
        self.main()

    def check_for_coords(self, x_val, y_val):
        new_coords = dict(x=x_val, y=y_val)
        result = [i for i in self.coords if all(i[target_key] == target_value for target_key, target_value in new_coords.items())]
        return result

    def add_coords(self, x_val, y_val):
        self.coords.append(dict(x=x_val, y=y_val))

    def process_direction(self, direction_char):
        if direction_char == ">":
            self.current_x += 1
        elif direction_char == "<":
            self.current_x -= 1
        elif direction_char == "^":
            self.current_y += 1
        elif direction_char == "v":
            self.current_y -= 1
        result = self.check_for_coords(self.current_x, self.current_y)
        if not result:
            self.add_coords(self.current_x, self.current_y)

    def main(self):
        input = utils.read_input("day_3_inputs")
        for character in input:
            self.process_direction(character)
        print(len(self.coords))


tracker = CoordinateTracker()