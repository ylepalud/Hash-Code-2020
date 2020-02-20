import io


class Parser:
    def __init__(self, path_to_input_file):
        self.input_file = path_to_input_file

    def parse(self):
        line_number = 0
        with io.open(self.input_file, "r", encoding="utf-8") as file:
            for line in file.readlines():
                line = line[:-1]
                if line_number == 0:
                    print(line)
                    pass
                if line_number == 1:
                    print(line)
                    pass
                else:
                    print(line)
                    pass
                line_number += 1
