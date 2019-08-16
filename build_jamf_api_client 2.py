import os
import logging
from pathlib import Path
import shutil

from build_jamf_core.create_project_structure import CreateProjectStructure
from build_jamf_core.get_url_extensions import GetUrlExtensions
from build_jamf_core.create_class import CreateClass
from build_jamf_core.human_assited_corrections import HumanCorrections
from build_jamf_core.clean_up_test_site import CleanUpSite

CreateProjectStructure().main()

for url_list in GetUrlExtensions().main():
    CreateClass(url_list).main()

# TODO now you need a script that cleans up the ones i cant account for.
HumanCorrections().main()

CleanUpSite().main()















# def get_trr_jamf_url_passed(self, url_extension):
#     """
#     If the url_extensions gets a 200 response then its a valid url extension.
#
#     Parameters
#     ----------
#     url_extension
#
#     Returns
#     -------
#         bool
#
#     """
#     test_url = requests.get(f'https://therealreal.jamfcloud.com/JSSResource{url_extension}',
#                             auth=HTTPBasicAuth(username, key), headers={'Accept': 'application/json'}).status_code
#     if test_url == 200:
#         url_pass = True
#     else:
#         url_pass = False
#
#     return url_pass
#
# def by_name_url_passed(self, url_extension):
#     """
#     If the url_extensions gets a 200 response then its a valid url extension.
#
#     Parameters
#     ----------
#     url_extension
#
#     Returns
#     -------
#         bool
#
#     """
#
#     test_url = requests.get(f'https://therealreal.jamfcloud.com/JSSResource{url_extension}',
#                             auth=HTTPBasicAuth(username, key), headers={'Accept': 'application/json'}).json()
#
#     first_key = list(test_url.keys())[0]
#     returned_item = test_url[first_key]
#     name_url = False
#     if type(returned_item) == list and len(returned_item) > 0:
#         if 'name' in list(returned_item[0].keys()):
#             name = returned_item[0]['name']
#
#             test_name_url = requests.get(
#                 f'https://therealreal.jamfcloud.com/JSSResource{url_extension}/name/{name}',
#                 auth=HTTPBasicAuth(username, key),
#                 headers={'Accept': 'application/json'}).status_code
#             if test_name_url == 200:
#                 name_url = True
#
#     return name_url
#
# def by_id_url_passed(self, url_extension):
#     """
#     If the url_extensions gets a 200 response then its a valid url extension.
#
#     Parameters
#     ----------
#     url_extension
#
#     Returns
#     -------
#         bool
#
#     """
#
#     test_url = requests.get(f'https://therealreal.jamfcloud.com/JSSResource{url_extension}',
#                             auth=HTTPBasicAuth(username, key), headers={'Accept': 'application/json'}).json()
#
#     first_key = list(test_url.keys())[0]
#     returned_item = test_url[first_key]
#     id_url = False
#     if type(returned_item) == list and len(returned_item) > 0:
#         if 'id' in list(returned_item[0].keys()):
#             url_id = returned_item[0]['id']
#
#             test_name_url = requests.get(
#                 f'https://therealreal.jamfcloud.com/JSSResource{url_extension}/id/{url_id}',
#                 auth=HTTPBasicAuth(username, key),
#                 headers={'Accept': 'application/json'}).status_code
#             if test_name_url == 200:
#                 id_url = True
#
#     return id_url
