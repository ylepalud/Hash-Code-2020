from model.Library import Library
import io


class ResultValue:
    def __init__(self):
        self.libraries = []

    def add_library(self, library: Library):
        self.libraries.append(library)

    def write_result(self, path_to_input_file: str):
        output_file_name = path_to_input_file.split(".")[0] + ".out"
        with io.open(output_file_name, "w+", encoding="utf-8") as file:
            file.write(str(len(self.libraries)) + '\n')
            for library in self.libraries:
                file.write(str(library))
        print("Solution store in ", output_file_name)
