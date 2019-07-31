from pathlib import Path
import logging


class CreateClassAttributes:
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
            f"    # TODO block this object from being used without using a search func.\n\n" \
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

    def attr_logic(self, url_data):
        url = url_data[0]
        rest_type = url_data[1]
        split_url = url.split("/")
        func_title = None
        func_params = None
        ext_url = None
        word_before_bracket = None
        if rest_type == 'get':
            loop_count = 0
            if "{" not in url:
                func_title = f'_{split_url[len(split_url) -1]}'
                func_params = ""
                ext_url = "/subset/basic"  # TODO fix this its super hacky no logic just works cause theres only one
            else:
                for text in split_url:
                    if loop_count <= 1:
                        loop_count += 1  # skipping the base url
                    elif loop_count == 2:
                        ext_url = f'/{text}'
                        word_before_bracket = text
                        loop_count += 1
                    else:
                        if self.has_bracket(text):
                            if text == "{start_date}_{end_date}":
                                text = "{start_date_end_date}"

                            if func_title:
                                if self.bracket_remover(text) == self.bracket_remover(word_before_bracket):
                                    func_title += f'_{self.bracket_remover(text)}'
                                else:
                                    func_title += f'_{self.bracket_remover(word_before_bracket)}'

                            else:
                                if self.bracket_remover(text) == self.bracket_remover(word_before_bracket):
                                    func_title = f'_{self.bracket_remover(text)}'
                                else:
                                    func_title = f'_{self.bracket_remover(word_before_bracket)}'

                            if func_params:
                                func_params += f', {self.bracket_remover(text)}'
                            else:
                                func_params = f', {self.bracket_remover(text)}'

                            ext_url += f'/{text}'

                        else:
                            ext_url += f'/{text}'
                            word_before_bracket = text

            self.create_text_for_attrs(func_title=func_title, func_params=func_params, ext_url=ext_url, url=url)

    def write_python_page(self, class_text):
        with open(Path(f"core/get_jamf/{self.file_name}.py"), "w") as writefile:
            writefile.write(class_text)

    def main(self):
        urls = self.url_index
        url_extension = urls[0][0]
        if "{" in url_extension:
            self.class_text = self.text_base_with_search_only_url(url_extension=url_extension)
        else:
            self.class_text = self.text_base(url_extension=url_extension)

        for url_data in urls:
            if url_data[0] == url_extension:
                if "{" in url_data[0]:  # this handles url structure that doesnt have a base url
                    self.attr_logic(url_data)
                else:
                    # TODO i think we can use this to create a Computers().name_id_list()
                    pass
            else:
                self.attr_logic(url_data)

        self.write_python_page(self.class_text)


