from time import sleep
import logging

from selenium.webdriver.chrome import webdriver

from script_files import import_login
from locators.insta_locators import InstaLocators

logger = logging.getLogger('scraping')  # singleton pattern


class Automation:
    def __init__(self, browser: webdriver):
        self.browser = browser
        self.login_info = import_login.Login_info()

    def login(self) -> bool:
        if len(self.login_info.info) < 1:
            return False
        self.browser.get("http://instagram.com")
        username = self.login_info.info[0]['username']
        password = self.login_info.info[0]['password']
        login_link = self.browser.find_element_by_xpath(InstaLocators.LOGIN_BOX)
        login_link.click()
        sleep(2)
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        # click on login button
        login_button = self.browser.find_element_by_xpath(InstaLocators.LOGIN_BUTTON)
        login_button.click()

        # click on Not Now (dont save login info)
        login_button = self.browser.find_element_by_xpath(InstaLocators.SAVE_INFO)
        login_button.click()

        # click on Not Now (turn on notifications)
        login_button = self.browser.find_element_by_xpath(InstaLocators.NOTIFICATIONS)
        login_button.click()
        return True

    def comment_something(self, url: str, message: str, number_of_times:int = 1) -> bool:
        """Comment a post number_of_times that you want

           number_of_times = 2 -> comment a post 2 times

           Returns:
               bool: return true if post all comments successfully

        """
        self.browser.get(url)
        for i in range(0, number_of_times):
            try:
                #click in the comment box
                comment_box = self.browser.find_element_by_xpath(InstaLocators.COMMENT_BOX)
                comment_box.click()

                #write stuff
                comment_box = self.browser.find_element_by_xpath(InstaLocators.COMMENT_BOX)
                comment_box.send_keys(message)

                #click on the publish
                comment_button = self.browser.find_element_by_xpath(InstaLocators.COMMENT_BUTTON)
                comment_button.click()
                logger.info('comment successfully')
                sleep(2)
            except:
                logger.error('some error when trying comment some stuff')
                return False

        return True

    def like_post(self, url: str):
        self.browser.get(url)
        aux = self.browser.find_element_by_css_selector("button div span svg._8-yf5")
        is_liked = aux.get_attribute('aria-label')
        if is_liked == 'Like':
            self.browser.implicitly_wait(5)
            like_button = self.browser.find_element_by_xpath(InstaLocators.LIKE_BUTTON)
            self.browser.implicitly_wait(5)
            like_button.click()

    def follow(self, username: str):
        self.browser.get("https://www.instagram.com/"+username)

        try:
            aux2 = self.browser.find_element_by_css_selector(InstaLocators.FOLLOW_BUTTON_PRIVATE)
            print(aux2.text)
            if aux2.text == 'Follow':
                aux2.click()
                print("oi")
            else:
                print('already following')
        except:
            try:
                aux = self.browser.find_element_by_css_selector(InstaLocators.FOLLOW_BUTTON)
                print(aux.text)

                if aux.text == 'Follow':
                    aux.click()
                    print("oi")
                else:
                    print('already following')
            except:
                print('already following')

