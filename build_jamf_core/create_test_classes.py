from pathlib import Path


class CreateTestClasses:
    def __init__(self, url):
        self.url = url

    def write_python_page(self, class_text):
        file_name = self.url.replace("/", "")
        with open(Path(f"core/tests/get_jamf/test_{file_name}.py"), "w") as writefile:
            writefile.write(class_text)

    def main(self):
        self.write_python_page(f"# TODO create test class for {self.url}")


