from pathlib import Path


class CreateTestClasses:
    file_name = None

    def __init__(self, url_index):
        self.url_index = url_index

    def text_base(self):
        text = f"from core.get_jamf.{self.file_name} import {self.file_name.capitalize()}\n\n\n" \
            f"def test_{self.file_name}():\n" \
            f"    assert {self.file_name.capitalize()}.status_code == 200\n\n"

        return text

    def write_python_page(self):
        if '{' in self.file_name:
            self.file_name = self.file_name.split('{')[0]
        with open(Path(f"core/tests/get_jamf/test_{self.file_name}.py"), "w") as writefile:
            writefile.write(self.text_base())

    def main(self):
        self.file_name = self.url_index[0][0].replace("/", "")
        self.write_python_page()



