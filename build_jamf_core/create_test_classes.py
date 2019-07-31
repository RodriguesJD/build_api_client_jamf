from pathlib import Path


class CreateTestClasses:
    def __init__(self, url_index):
        self.url_index = url_index

    def write_python_page(self, class_text):
        file_name = self.url_index[0][0].replace("/", "")
        with open(Path(f"core/tests/get_jamf/test_{file_name}.py"), "w") as writefile:
            writefile.write(class_text)

    def main(self):
        self.write_python_page(f"# TODO create test class for {self.url_index[0][0]}")
        print('\n')
        print(self.url_index)


