import utils

class CoordinateTracker:

    def __init__(self):
        self.coords = []
        self.santa_current_x = 0
        self.santa_current_y = 0
        self.robot_current_x = 0
        self.robot_current_y = 0
        self.current_move="santa"
        self.main()

    def check_for_coords(self, x_val, y_val):
        new_coords = dict(x=x_val, y=y_val)
        result = [i for i in self.coords if all(i[target_key] == target_value for target_key, target_value in new_coords.items())]
        return result

    def add_coords(self, x_val, y_val):
        self.coords.append(dict(x=x_val, y=y_val))

    def process_direction(self, direction_char):
        x = 0
        y = 0
        if direction_char == ">":
            x += 1
        elif direction_char == "<":
            x -= 1
        elif direction_char == "^":
            y += 1
        elif direction_char == "v":
            y -= 1

        if self.current_move == "santa":
            self.current_move = "robot"
            self.santa_current_x += x
            self.santa_current_y += y
            current_x = self.santa_current_x
            current_y = self.santa_current_y
        elif self.current_move == "robot":
            self.current_move = "santa"
            self.robot_current_x += x
            self.robot_current_y += y
            current_x = self.robot_current_x
            current_y = self.robot_current_y

        result = self.check_for_coords(current_x, current_y)
        if not result:
            self.add_coords(current_x, current_y)

    def main(self):
        input = utils.read_input("day_3_inputs")
        for character in input:
            self.process_direction(character)
        print(len(self.coords))


tracker = CoordinateTracker()