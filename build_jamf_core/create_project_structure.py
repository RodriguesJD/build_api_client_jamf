import os
from pathlib import Path


class CreateProjectStructure:
    """
    The build_jamf_api_client project needs dir and files before
    """
    base_dir = "core"
    tests_dir = f"{base_dir}/tests/"
    get_dir = f"{base_dir}/get_jamf/"
    get_file = f"{get_dir}/get_jamf.py"
    config_file = f"{base_dir}/config.py"
    init_file = "__init__.py"

    def create_base_dir(self):
        if not os.path.isdir(Path(self.base_dir)):
            os.mkdir(Path(self.base_dir))
            open(Path(f"{self.base_dir}/{self.init_file}"), 'a').close()

    def create_tests_dir(self):
        if not os.path.isdir(Path(self.tests_dir)):
            os.mkdir(Path(self.tests_dir))
            open(Path(f"{self.tests_dir}/{self.init_file}"), 'a').close()

    def create_get_dir(self):
        if not os.path.isdir(Path(self.get_dir)):
            os.mkdir(Path(self.get_dir))
            open(Path(f"{self.get_dir}/{self.init_file}"), 'a').close()

    def create_get_file(self):
        self_url_fixer = "{self.url}"
        base_url_fixer = "{config.base_url}"
        accept_fixer = "{'Accept': 'application/json'}"
        text_file = f"""from requests.auth import HTTPBasicAuth
import requests

from core.secret.key import key, username
from core import config


class GetJamf:

    url = None

    def get_jamf(self):
        return requests.get(f'{base_url_fixer}{self_url_fixer}',
                            auth=HTTPBasicAuth(username, key), headers={accept_fixer})\n"""
        if not os.path.isfile(self.get_file):
            with open(Path(self.get_file), "w") as writefile:
                writefile.write(text_file)

    def create_config_file(self):
        text_file = "base_url = None"
        if not os.path.isfile(self.config_file):
            with open(Path(self.config_file), "w") as writefile:
                writefile.write(text_file)

    def main(self):
        self.create_base_dir()
        self.create_tests_dir()
        self.create_get_dir()
        self.create_get_file()
        self.create_config_file()


