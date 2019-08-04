from pathlib import Path

from build_jamf_core.create_methods_for_get_class import MethodLogic


class CreateClass:

    class_text = ""

    def __init__(self, url_index):
        self.url_index = url_index

    def correct_base_url(self):
        url = self.url_index[0][0]
        url_components = url.split("/")
        base_url = "/" + url_components[1]
        return base_url


    def text_base(self):
        """
        This creates the imports and basic class sturcutre
        """
        class_title = self.url_index[0][0].replace('/', '').capitalize()
        if "{" in class_title:
            # Remove search paramater form class title. Complex_search_urls cause this.
            class_title = class_title.split("{")[0]

        base_url = self.url_index[0][0]
        if len(base_url.split("/")) > 2:
            base_url = self.correct_base_url()

        text = f"from core.get_jamf.get_jamf import GetJamf\n\n\n" \
            f"class {class_title}(GetJamf):\n\n" \
            f"    url = '{base_url}'\n\n"

        return text

    def create_file(self):
        """
        Creates the python file and writes the class and its methods.
        :return:
        """
        file_name = self.url_index[0][0].replace("/", "") + ".py"
        if "{" in file_name:
            # Remove search paramater form file name. Complex_search_urls cause this.
            file_name = file_name.split("{")[0] + ".py"

        with open(Path(f"core/get_jamf/{file_name}"), "w") as writefile:
            writefile.write(self.text_base())
            writefile.write(self.class_text)

    def main(self):
        create_file_flag = False
        for url_data in self.url_index:
            url = url_data[0]
            rest_type = url_data[1]
            if rest_type == 'get':
                func_text = MethodLogic(url, rest_type).main()

                if func_text and not create_file_flag:  # If this condition is met then create the file
                    # print(f"--{url_data}")
                    self.class_text += func_text
                    create_file_flag = True  # I only need to create files if func_data is returned

                elif func_text and create_file_flag:  # if file is being created then add this method
                    # print(f"--{url_data}")
                    self.class_text += func_text

        if create_file_flag:
            self.create_file()


