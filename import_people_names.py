from time import sleep

from selenium.webdriver.chrome import webdriver
from locators.insta_locators import InstaLocators


class ImportPeopleNames:

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.data = []

    def _is_unique(self, name: str):
        pass

    def _import_names_from_file(self):
        with open("people_names.txt") as file:
            self.data = [aux.strip() for aux in file.readlines()]

    def read_comments(self):
        while True:
            try:
                login_link = self.browser.find_element_by_xpath(InstaLocators.LOAD_MORE_COMMENTS)
                login_link.click()
            except Exception as e:
                break
        x = self.browser.find_elements_by_css_selector(InstaLocators.LIST_OF_COMMENTS)
        for i in x:
            print(i.text)

        print(len(x))

    def get_names(self, limit: int):
        follow_section = self.browser.find_element_by_xpath(InstaLocators.FOLLOWS_SECTIONS)
        follow_section.click()

        fBody = self.browser.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        pre=0
        times=0
        while scroll < 1000000:  # scroll 5 times
            self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            scroll += 1
            actu= len(self.browser.find_elements_by_css_selector("li.wo9IH"))
            if actu != pre and actu < limit:
                pre = actu
                times = 0
            elif actu == pre and times < 300 and actu < limit:
                times += 1
            else:
                break
        x = self.browser.find_elements_by_css_selector(InstaLocators.LIST_OF_FOLLOWS)
        f = open("people_names.txt", "a")
        for i in x:
            if i.text not in self.data:
                f.write(i.text+"\n")
        f.close()