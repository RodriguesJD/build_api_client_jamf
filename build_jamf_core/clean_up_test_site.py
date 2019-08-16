import os
import shutil


class CleanUpSite:

    def clean_up_test_site(self):
        core_dir = os.listdir('base_core/core/')
        for item in core_dir:
            if "__" in item:
                pass
            elif item == "secret":
                pass
            elif item == "build_jamf_client":
                pass
            elif item == "config.py":
                pass
            elif item == "tests":
                shutil.rmtree(f"base_core/core/{item}")
            else:
                if os.path.isfile(f"base_core/core/{item}"):
                    os.remove(f"base_core/core/{item}")
                else:
                    shutil.rmtree(f"base_core/core/{item}")

    def main(self):
        clean_up = input("Clean up. Y for yes, any other key mean no\n")
        if clean_up.lower() == "y":
            self.clean_up_test_site()