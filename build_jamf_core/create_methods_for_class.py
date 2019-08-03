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

    def separate_url_by_slash(self):
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

        if len(self.separate_url_by_slash()) == 2:  # Example /accounts len is equal to 2.
            base_url = True
        else:
            base_url = False

        return base_url

    def is_simple_search_url(self):
        """
        Validate that the url is the base url. Example is Class Accounts has a base url /accounts that returns basic
        info like id and name of each account.
        :return:
        """

        if len(self.separate_url_by_slash()) == 4:  # Example /accounts len is equal to 2.
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
        func_title = self.separate_url_by_slash()[2]
        search_paramater = self.separate_url_by_slash()[3].replace("{", "").replace("}", "")
        url_extension = self.url.replace(f"/{self.separate_url_by_slash()[1]}", "")

        text = f'    def by_{func_title}(self, {search_paramater}):\n' \
            f'        self.url = {f_string_handler}{url_extension}"\n' \
            f'        return self.get_jamf()\n\n'

        return text

    def main(self):
        func_text = None
        if self.is_base_url() and self.is_status_200():
            func_text = self.create_func_text_for_base_url()

        elif self.is_simple_search_url():
            func_text = self.create_func_text_for_simple_search_url()

        return func_text

