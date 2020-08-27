from time import sleep

from selenium.webdriver.chrome import webdriver


class ImportPeopleNames:

    def __init__(self, browser: webdriver):
        self.browser = browser

    def read_comments(self):
        while True:
            try:
                login_link = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button")
                login_link.click()
            except Exception as e:
                break
        print("conseguiu")
        x = self.browser.find_elements_by_css_selector("a.sqdOP.yWX7d._8A5w5.ZIAjV")
        for i in x:
            print(i.text)

        print(len(x))

    def get_names(self, limit:int):
        login_link = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]")
        login_link.click()

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
        print(actu)
        print("ended")
        x = self.browser.find_elements_by_css_selector("li div div div div span a.FPmhX.notranslate._0imsa")
        f = open("people_names.txt", "a")
        for i in x:
            f.write(i.text+"\n")
