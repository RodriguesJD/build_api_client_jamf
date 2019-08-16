import requests
from requests.auth import HTTPBasicAuth
import os
from pprint import pprint


class MethodLogic:

    base_url = os.environ["JAMF_URL_PROD"]
    key = os.environ["JAMF_KEY"]
    username = os.environ["JAMF_USERNAME"]
    jamf_id = None  # if

    def __init__(self, url, rest_type):
        self.url = url
        self.rest_type = rest_type

    def url_components(self):
        """
        Divides the url up by each /
        :return:
        """
        return self.url.split("/")

    def is_status_200(self):
        """
        Validate the the url is functioning
        :return:
        """
        # try a rest api get request using url
        try:
            jamf_reguest = requests.get(f'{self.base_url}{self.url}',
                                        auth=HTTPBasicAuth(self.username, self.key),
                                        headers={'Accept': 'application/json'})
        except ValueError:
            jamf_reguest = False

        # get status code if request passed
        if jamf_reguest:
            status_code = jamf_reguest.status_code
        else:
            status_code = False

        # Validate that status code passes
        if status_code == 200:
            status = True
        else:
            status = False

        return status

    def is_base_url(self):
        """
        Validate that the url is the base url. Example is Class Accounts has a base url /accounts that returns basic
        info like id and name of each account.
        :return:
        """

        if len(self.url_components()) == 2:  # Example /accounts len is equal to 2.
            base_url = True
        else:
            base_url = False

        return base_url

    def is_simple_search_url(self):
        """
        Simple search means the url_components length is 4 and it has 1 search parameter.
        :return:
        """

        if len(self.url_components()) == 4:
            base_url = True
        else:
            base_url = False

        return base_url

    def is_elongated_simple_search(self):
        """
        Simple search means the url_components length is 5 and it has 1 search parameter.
        :return:
        """
        search_components = 0
        if len(self.url_components()) == 5:
            for component in self.url_components():
                if "{" in component:
                    search_components += 1

        if search_components == 1:
            base_url = True
        else:
            base_url = False

        return base_url

    def is_complex_search_url(self):
        """
        Complex search means the url_components length is 5 and it needs 2 search parameters.
        :return:
        """
        search_components = 0
        if len(self.url_components()) == 5:
            for component in self.url_components():
                if "{" in component:
                    search_components += 1

        if search_components == 2:
            base_url = True
        else:
            base_url = False

        return base_url

    def is_elongated_complex_search_url(self):
        """
        Complex search means the url_components length is 6 and it needs 2 search parameters.
        :return:
        """
        search_components = 0
        if len(self.url_components()) == 6:
            for component in self.url_components():
                if "{" in component:
                    search_components += 1

        if search_components == 2:
            base_url = True
        else:
            base_url = False

        return base_url

    def is_seven_complex_search_url(self):
        """
                Complex search means the url_components length is 7 and it needs 3 search parameters.
                :return:
                """
        search_components = 0
        if len(self.url_components()) == 7:
            for component in self.url_components():
                if "{" in component:
                    search_components += 1

        if search_components == 3:
            base_url = True
        else:
            base_url = False

        return base_url

    def is_eight_complex_search_url(self):
        """
        Complex search means the url_components length is 8 and it needs 3 search parameters.
        :return:
        """
        search_components = 0
        if len(self.url_components()) == 8:
            for component in self.url_components():
                if "{" in component:
                    search_components += 1

        if search_components == 3:
            base_url = True
        else:
            base_url = False

        return base_url

    def create_func_text_for_base_url(self):
        f_string_handler = 'f"{self.url}'
        text = f'    def base_info(self):\n' \
            f'        self.url = {f_string_handler}"\n' \
            f'        return self.get_jamf()\n\n'

        return text

    def create_func_text_for_simple_search_url(self):
        f_string_handler = 'f"{self.url}'
        func_title = self.url_components()[2]
        search_paramater = self.url_components()[3].replace("{", "").replace("}", "")
        url_extension = self.url.replace(f"/{self.url_components()[1]}", "")

        text = f'    def by_{func_title}(self, {search_paramater}):\n' \
            f'        self.url = {f_string_handler}{url_extension}"\n' \
            f'        return self.get_jamf()\n\n'

        return text

    def create_func_text_for_elongated_simple_search_url(self):
        f_string_handler = 'f"{self.url}'
        func_title = f"{self.url_components()[2]}_{self.url_components()[3]}"
        search_paramater = self.url_components()[4].replace("{", "").replace("}", "")
        url_extension = self.url.replace(f"/{self.url_components()[1]}", "")

        text = f'    def by_{func_title}(self, {search_paramater}):\n' \
            f'        self.url = {f_string_handler}{url_extension}"\n' \
            f'        return self.get_jamf()\n\n'

        return text

    def create_func_text_for_complex_search_url(self):
        f_string_handler = 'f"{self.url}'
        func_title = self.url_components()[2]
        func_title_extension = self.url_components()[4].replace("{", "").replace("}", "")
        if func_title_extension != "start_date_end_date" and func_title_extension != 'interval':
            print(self.url)
            print(len(self.url_components()))
            raise Exception(f"There is an unaccounted var: {func_title_extension} ")

        elif func_title == '{log}':
            func_title = func_title.replace("{", "").replace("}", "")
            search_paramater = func_title
            second_search_param = self.url_components()[4].replace("{", "").replace("}", "")
            url_extension = self.url.replace(f"/{self.url_components()[1]}", "")
        else:
            search_paramater = self.url_components()[3].replace("{", "").replace("}", "")
            url_extension = self.url.replace(f"/{self.url_components()[1]}", "")
            second_search_param = "start_date, end_date"

        text = f'    def by_{func_title}_and_dates(self, {search_paramater}, {second_search_param}):\n' \
            f'        self.url = {f_string_handler}{url_extension}"\n' \
            f'        return self.get_jamf()\n\n'
        return text

    def create_func_text_for_elongated_complex_search_url(self):
        f_string_handler = 'f"{self.url}'
        func_title = f'{self.url_components()[3].replace("{", "").replace("}", "")}_' \
            f'{self.url_components()[5].replace("{", "").replace("}", "")}'

        search_paramater1 = self.url_components()[3].replace("{", "").replace("}", "")
        search_paramater2 = self.url_components()[5].replace("{", "").replace("}", "")
        url_extension = self.url.replace(f"/{self.url_components()[1]}", "")

        text = f'    def by_{func_title}(self, {search_paramater1}, {search_paramater2}):\n' \
            f'        self.url = {f_string_handler}{url_extension}"\n' \
            f'        return self.get_jamf()\n\n'

        return text

    def create_func_text_for_seven_complex_search_url(self):
        if self.url != "/computerhardwaresoftwarereports/id/{id}/{start_date}_{end_date}/subset/{subset}":
            raise Exception("create_func_text_for_seven_complex_search_url only accounts for computerhardwaresoftwarereports")
        f_string_handler = 'f"{self.url}'
        func_title = f'{self.url_components()[3].replace("{", "").replace("}", "")}_' \
            f'{self.url_components()[5].replace("{", "").replace("}", "")}'

        search_paramater1 = self.url_components()[3].replace("{", "").replace("}", "")
        search_paramater2 = self.url_components()[4].replace("{", "").replace("}", "")
        search_paramater3 = self.url_components()[6].replace("{", "").replace("}", "")
        url_extension = self.url.replace(f"/{self.url_components()[1]}", "")

        text = f'    def by_computerhardwaresoftwarereports_id_subset(self, {search_paramater1}, {search_paramater2}, {search_paramater3}):\n' \
            f'        self.url = {f_string_handler}{url_extension}"\n' \
            f'        return self.get_jamf()\n\n'

        return text

    def create_func_text_for_eight_complex_search_url(self):
        f_string_handler = 'f"{self.url}'
        func_title = f'{self.url_components()[3].replace("{", "").replace("}", "")}_' \
            f'{self.url_components()[5].replace("{", "").replace("}", "")}_{self.url_components()[7].replace("{", "").replace("}", "")}'

        search_paramater1 = self.url_components()[3].replace("{", "").replace("}", "")
        search_paramater2 = self.url_components()[5].replace("{", "").replace("}", "")
        search_paramater3 = self.url_components()[7].replace("{", "").replace("}", "")
        url_extension = self.url.replace(f"/{self.url_components()[1]}", "")

        text = f'    def by_(self, {search_paramater1}, {search_paramater2}, {search_paramater3}):\n' \
            f'        self.url = {f_string_handler}{url_extension}"\n' \
            f'        return self.get_jamf()\n\n'
        return text

    def main(self):
        func_text = None

        if self.is_base_url() and self.is_status_200():
            func_text = self.create_func_text_for_base_url()

        elif self.is_simple_search_url():
            func_text = self.create_func_text_for_simple_search_url()

        elif self.is_elongated_simple_search():
            func_text = self.create_func_text_for_elongated_simple_search_url()

        elif self.is_complex_search_url():
            func_text = self.create_func_text_for_complex_search_url()

        elif self.is_elongated_complex_search_url():
            func_text = self.create_func_text_for_elongated_complex_search_url()

        elif self.is_seven_complex_search_url():
            func_text = self.create_func_text_for_seven_complex_search_url()

        elif self.is_eight_complex_search_url():
            func_text = self.create_func_text_for_eight_complex_search_url()

        else:
            # print(self.url)
            # print(len(self.url_components()))
            pass
        if type(func_text) == bool:
            print(func_text)
            input()
        return func_text

