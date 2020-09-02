import configparser
import logging
from telnetlib import EC
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.fake_account_locators import FakeAcoountsLocators

logger = logging.getLogger('scraping')  # singleton pattern

class FakeAccount:

    emails = []
    template_email=""
    password = ""

    def __init__(self, browser: webdriver):
        self.browser = browser
        self._load_emails_password()
    """
    def __init__(self):
        pass
    """

    def create_email(self):
        self.browser.get("https://mail.tutanota.com/login")
        more_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.MORE_BUTTON)
        more_button.click()
        register_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.REGISTER_BUTTON)
        register_button.click()
        while True:
            try:
                subscription_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.FREE_SUBSCRIPTION)
                subscription_button.click()
                confirmation_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.CONFIRMATION_BUTTON)
                confirmation_button.click()
                break
            except:
                pass
            sleep(0.5)

        email_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.EMAIL_ADDRESS)
        email_button.click()
        email_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.EMAIL_ADDRESS)
        email_button.send_keys(self.template_email)

        password_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.PASSWORD)
        password_button.click()
        password_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.PASSWORD2)
        password_button.send_keys(self.password)

        repeat_password_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.REPEAT_PASSWORD)
        repeat_password_button.click()
        repeat_password_button = self.browser.find_element_by_xpath(FakeAcoountsLocators.REPEAT_PASSWORD)
        repeat_password_button.send_keys(self.password)

        checkbox = self.browser.find_element_by_xpath(FakeAcoountsLocators.AGREE_TERMS)
        checkbox.click()

        checkbox2 = self.browser.find_element_by_xpath(FakeAcoountsLocators.AT_LEAST_16)
        checkbox2.click()




    def _load_emails_password(self):
        with open("fake_accounts/email.txt", "r") as file:
            data = [aux.strip() for aux in file.readlines()]
            for i in range(0, len(data)):
                if len(data[i]) > 2:
                    self.emails.append(data[i])

        config = configparser.ConfigParser()
        config.sections()
        config.read('fake_accounts/template_for_emails.ini')
        self.password = config['DEFAULT']['password']
        self.template_email = config['DEFAULT']['name_to_email']

        print(self.emails)
        print(self.password)
        print(self.template_email)