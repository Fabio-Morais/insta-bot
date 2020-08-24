from time import sleep
import logging

from selenium.webdriver.chrome import webdriver


from locators.insta_locators import instaLocators

logger = logging.getLogger('scraping')  # singleton pattern


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

    def comment_something(self, number_of_times:int,number_of_identifications:int = 0) -> bool:
        """Comment a post number_of_times that you want

           number_of_times = 2 -> comment a post 2 times

           Returns:
               bool: return true if post all comments successfully

           """
        for i in range(0, number_of_times):
            try:
                #click in the comment box
                comment_box = self.browser.find_element_by_xpath(instaLocators.COMMENT_BOX)
                comment_box.click()

                #write stuff
                comment_box = self.browser.find_element_by_xpath(instaLocators.COMMENT_BOX)
                comment_box.send_keys("ola")

                #click on the publish
                comment_button = self.browser.find_element_by_xpath(instaLocators.COMMENT_BUTTON)
                comment_button.click()
                logger.info('comment successfully')
                sleep(2)
            except:
                logger.error('some error when trying comment some stuff')
                return False

        return True

    def like_post(self):
        aux = self.browser.find_element_by_css_selector("button div span svg._8-yf5")
        is_liked = aux.get_attribute('aria-label')
        if is_liked == 'Like':
            self.browser.implicitly_wait(5)
            like_button = self.browser.find_element_by_xpath(instaLocators.LIKE_BUTTON)
            self.browser.implicitly_wait(5)
            like_button.click()

    def follow(self):
        try:
            aux = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button")
            print(aux.text)
            if aux.text == 'Follow':
                aux.click()
            else:
                print('already following')
        except:
            print('Private profile')
            try:
                aux2 = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/button")
                aux2.click()
            except:
                print('rip')
