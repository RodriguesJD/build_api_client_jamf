from pathlib import Path
import logging
from build_jamf_core.create_methods_for_get_class import MethodLogic


class CreateClass:
    """
    Create python text files
    """
    lb = "\n"
    class_text = None
    file_name = None

    def __init__(self, url_index):
        self.url_index = url_index

    def text_base(self, url_extension):
        self.file_name = url_extension.replace('/', '')
        text = f"from core.get_jamf.get_jamf import GetJamf\n\n\n" \
            f"class {url_extension.replace('/', '').capitalize()}(GetJamf):\n\n" \
            f"    url = '{url_extension}'\n\n"

        return text

    def text_base_with_search_only_url(self, url_extension):
        url = url_extension.split("/")[1]
        self.file_name = url
        text = f"from core.get_jamf.get_jamf import GetJamf\n\n\n" \
            f"class {url.capitalize()}(GetJamf):\n\n" \
            f"    url = '/{url}'\n\n"

        return text

    def create_text_for_attrs(self, func_title, func_params, ext_url, url):
        f_string_handler = 'f"{self.url}'
        text = f'    def by{func_title}(self{func_params}):\n' \
            f'        self.url = {f_string_handler}{ext_url}"\n' \
            f'        return self.get_jamf()\n\n'

        self.class_text += text

    def has_bracket(self, text):
        if "{" in text:
            bracket = True
        else:
            bracket = False

        return bracket

    def bracket_remover(self, text_with_brackets):
        return text_with_brackets.replace("{", "").replace("}", "")

    def write_python_page(self, class_text):
        with open(Path(f"base_core/core/get_jamf/{self.file_name}.py"), "w") as writefile:
            writefile.write(class_text)

    def main(self):
        urls = self.url_index  # set of url exenstions per rest api FEATURE
        url_extension_base = urls[0][0]
        if "{" in url_extension_base:  # if { is in the url_extension_base its a search only url
            self.class_text = self.text_base_with_search_only_url(url_extension=url_extension_base)
        else:
            self.class_text = self.text_base(url_extension=url_extension_base)

        for url_data in urls:
            url = url_data[0]
            rest_type = url_data[1]

            if rest_type == 'get':
                method_logic = MethodLogic(url, rest_type).main()
                if method_logic:
                    self.class_text += method_logic

        self.write_python_page(self.class_text)


