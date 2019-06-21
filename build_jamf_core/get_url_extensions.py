import time
from selenium import webdriver
from bs4 import BeautifulSoup
from build_jamf_core.config import base_url, path_to_chrome_driver



class GetUrlExtensions:
    """
    Scrapes jamf instance and gets all the url extensions.
    """

    browser = webdriver.Chrome(path_to_chrome_driver)
    usable_extensions = []

    url = base_url

    def get_page(self):
        """
        Update the browser object with the url that is passed to the class.

        """
        self.browser.get(self.url)

    def get_bs4_html(self):
        return BeautifulSoup(self.browser.page_source, features="lxml")

    def get_all_url_extensions(self):
        rest_type = None
        html = self.get_bs4_html().text.split("\n")
        for url_extension in html:
            if url_extension:
                first_character = url_extension[0]
                if "/" in first_character and rest_type:
                    if len(rest_type) < 7: # five is larger than delete with is the largest rest_type
                        self.usable_extensions.append([url_extension, rest_type])

                else:
                    rest_type = url_extension

    def sorted_urls(self):
        api_urls = []
        url_extensions = self.usable_extensions
        # url_extensions = GetUrlExtensions(url).main()
        used_url_ext = []
        for url_extension in url_extensions:
            if url_extension[1] == 'Response Headers':
                pass
            else:
                list_of_urls = [url_extension]
                ext_base = url_extension[0].split("/")[1]
                if ext_base in used_url_ext:
                    pass
                else:
                    used_url_ext.append(ext_base)
                    for url_collector in url_extensions:
                        collect_base = url_collector[0].split("/")[1]
                        if url_extension[0] == url_collector[0]:
                            pass
                        elif ext_base == collect_base:
                            list_of_urls.append(url_collector)

                    api_urls.append(list_of_urls)

        return api_urls

    def main(self):
        self.get_page()  # open the webpage object
        time.sleep(2)  # Allow page to populate
        self.get_all_url_extensions()  # Create class list for all url extension
        self.browser.close()  # The browser object is no longer needed
        return self.sorted_urls()

