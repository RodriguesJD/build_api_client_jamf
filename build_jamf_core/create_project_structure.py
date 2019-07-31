import os
from pathlib import Path


class CreateProjectStructure:
    """
    The build_jamf_api_client project needs dir and files before
    """
    base_dir = "core"
    tests_dir = f"{base_dir}/tests/"
    test_get_dir = f"{base_dir}/tests/get_jamf/"
    get_dir = f"{base_dir}/get_jamf/"
    get_file = f"{get_dir}get_jamf.py"
    init_file = "__init__.py"

    def create_base_dir(self):
        if not os.path.isdir(Path(self.base_dir)):
            print(f"Create {self.base_dir} directory")
            os.mkdir(Path(self.base_dir))
            open(Path(f"{self.base_dir}/{self.init_file}"), 'a').close()
        else:
            print(f"{self.base_dir} exists.")

    def create_tests_dir(self):
        if not os.path.isdir(Path(self.tests_dir)):
            print(f"Create {self.tests_dir} directory")
            os.mkdir(Path(self.tests_dir))
            open(Path(f"{self.tests_dir}/{self.init_file}"), 'a').close()
        else:
            print(f"{self.tests_dir} exists.")

    def create_get_dir(self):
        if not os.path.isdir(Path(self.get_dir)):
            print(f"Create {self.get_dir} directory")
            os.mkdir(Path(self.get_dir))
            open(Path(f"{self.get_dir}/{self.init_file}"), 'a').close()
        else:
            print(f"{self.get_dir} exists.")

    def create_test_get_dir(self):
        if not os.path.isdir(Path(self.test_get_dir)):
            print(f"Create {self.test_get_dir} directory")
            os.mkdir(Path(self.test_get_dir))
            open(Path(f"{self.test_get_dir}/{self.init_file}"), 'a').close()
        else:
            print(f"{self.create_tests_dir()} exists.")

    def create_get_file(self):
        print(f"Create {self.get_file} file")
        self_url_fixer = "{self.url}"
        base_url_fixer = "{base_url}"
        accept_fixer = "{'Accept': 'application/json'}"
        text_file = f"""from requests.auth import HTTPBasicAuth
import requests
import os

base_url = os.environ["JAMF_URL_PROD"]
key = os.environ["JAMF_KEY"]
username = os.environ["JAMF_USERNAME"]


class GetJamf:

    url = None

    def get_jamf(self):
        return requests.get(f'{base_url_fixer}{self_url_fixer}',
                            auth=HTTPBasicAuth(username, key), headers={accept_fixer})\n"""
        if not os.path.isfile(self.get_file):
            with open(Path(self.get_file), "w") as writefile:
                writefile.write(text_file)
        else:
            print(f"{self.get_file} exists.")

    def main(self):
        self.create_base_dir()
        self.create_tests_dir()
        self.create_get_dir()
        self.create_test_get_dir()
        self.create_get_file()
        print("\n")


