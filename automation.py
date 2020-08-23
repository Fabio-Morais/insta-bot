from telnetlib import EC
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.insta_locators import instaLocators


class Automation:
    def __init__(self, browser: webdriver):
        self.browser = browser

    def login(self):
        login_link = self.browser.find_element_by_xpath(instaLocators.LOGIN_BOX)
        login_link.click()
        sleep(2)
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys("fabiouds12345")
        password_input.send_keys("catarina12345")

        # click on login button
        login_button = self.browser.find_element_by_xpath(instaLocators.LOGIN_BUTTON)
        login_button.click()

        # click on Not Now (dont save login info)
        login_button = self.browser.find_element_by_xpath(instaLocators.SAVE_INFO)
        login_button.click()

        # click on Not Now (turn on notifications)
        login_button = self.browser.find_element_by_xpath(instaLocators.NOTIFICATIONS)
        login_button.click()


    def comment_something(self):
        #click in the comment box
        comment_box = self.browser.find_element_by_xpath(instaLocators.COMMENT_BOX)
        comment_box.click()

        #write stuff
        comment_box = self.browser.find_element_by_xpath(instaLocators.COMMENT_BOX)
        comment_box.send_keys("ola")

        #click on the publish
        comment_button = self.browser.find_element_by_xpath(instaLocators.COMMENT_BUTTON)
        comment_button.click()


    def like_post(self):
        aux = self.browser.find_element_by_css_selector("button div span svg._8-yf5")
        is_liked = aux.get_attribute('aria-label')
        if is_liked == 'Like':
            self.browser.implicitly_wait(5)
            like_button = self.browser.find_element_by_xpath(instaLocators.LIKE_BUTTON)
            self.browser.implicitly_wait(5)
            like_button.click()



