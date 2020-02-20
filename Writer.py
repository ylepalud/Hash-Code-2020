import io


class Writer:
    def __init__(self):
        pass

    def write_out_put(self, path_to_input_file, data):
        output_file_name = path_to_input_file.split(".")[0] + ".out"
        with io.open(output_file_name, "w+", encoding="utf-8") as file:
            file.write(data)
