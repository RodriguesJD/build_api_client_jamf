import os
import logging
from pathlib import Path
import shutil

from build_jamf_core.create_project_structure import CreateProjectStructure
from build_jamf_core.get_url_extensions import GetUrlExtensions
from build_jamf_core.create_class_attributes import CreateClassAttributes
from build_jamf_core.human_assited_corrections import HumanCorrections
from build_jamf_core.create_test_classes import CreateTestClasses

CreateProjectStructure().main()

for url_list in GetUrlExtensions().main():
    CreateClassAttributes(url_list).main()
    CreateTestClasses(url_list[0][0]).main()

# TODO now you need a script that cleans up the ones i cant account for.
# HumanCorrections().main()


def clean_up_test_site():
    core_dir = os.listdir('core/')
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
            shutil.rmtree(f"core/{item}")
        else:
            if os.path.isfile(f"core/{item}"):
                os.remove(f"core/{item}")
            else:
                shutil.rmtree(f"core/{item}")


clean_up = input("Clean up. Y for yes, any other key mean no\n")
if clean_up.lower() == "y":
    clean_up_test_site()

# TODO move project over to jamf-api-client for commiting changes

