import os
from pathlib import Path


class HumanCorrections:

    get_jamf_dir = Path("base_core/core/get_jamf")

    def any_duplicate_functions(self, class_item):
        file = Path(f"{self.get_jamf_dir}/{class_item}")
        with open(file, "r") as open_file:
            python_file = open_file.readlines()
            list_of_func = []
            for line in python_file:
                if "by_" in line:
                    func_name = line.split("by_")[1].split("(")[0]
                    if func_name in list_of_func:
                        print(f"{class_item} has duplicate function names.")
                    else:
                        list_of_func.append(func_name)

    def main(self):
        for item in os.listdir(Path(self.get_jamf_dir)):
            if item == "__pycache__":
                pass
            elif item == "__init.py":
                pass
            elif item == "get_jamf.py":
                pass
            else:
                self.any_duplicate_functions(item)
