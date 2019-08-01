import os
import logging
from pathlib import Path
import shutil

from build_jamf_core.create_project_structure import CreateProjectStructure
from build_jamf_core.get_url_extensions import GetUrlExtensions
# from build_jamf_core.create_class import CreateClass
from build_jamf_core.human_assited_corrections import HumanCorrections
from build_jamf_core.create_test_classes import CreateTestClasses
from build_jamf_core.dev_create_class import CreateClass

CreateProjectStructure().main()

for url_extension in GetUrlExtensions().main():
    print("URL EXTENSION SET")
    CreateClass(url_extension).main()
#     CreateTestClasses(url_list).main()
#
# # TODO now you need a script that cleans up the ones i cant account for.
# HumanCorrections().main()

clean_up = input("Clean up. Y for yes, any other key mean no\n")
if clean_up.lower() == "y":
    shutil.rmtree(Path(f"core/"))

# TODO move project over to jamf-api-client for commiting changes

