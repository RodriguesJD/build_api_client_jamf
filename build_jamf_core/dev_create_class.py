from pathlib import Path

from build_jamf_core.create_methods_for_class import MethodLogic


class CreateClass:

    class_text = ""

    def __init__(self, url_index):
        self.url_index = url_index

    def text_base(self):
        text = f"from core.get_jamf.get_jamf import GetJamf\n\n\n" \
            f"class {self.url_index[0][0].replace('/', '').capitalize()}(GetJamf):\n\n" \
            f"    url = '{self.url_index[0][0]}'\n\n"

        return text

    def create_file(self):
        file_name = self.url_index[0][0].replace("/", "") + ".py"

        with open(Path(f"core/get_jamf/{file_name}"), "w") as writefile:
            writefile.write(self.text_base())
            writefile.write(self.class_text)

    def main(self):
        create_file_flag = False
        for url_data in self.url_index:
            url = url_data[0]
            rest_type = url_data[1]
            func_text = MethodLogic(url, rest_type).main()
            if func_text:
                print(f"--{url_data}")
                self.class_text += func_text
                create_file_flag = True  # I only need to create files if func_data is returned

        if create_file_flag:
            self.create_file()
            

