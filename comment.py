class comment:
    def __init__(self, browser):
        self.browser = browser

    def comment_something(self):
        #click in the comment box
        comment_box = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
        comment_box.click()

        #write stuff
        comment_input = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
        comment_input.send_keys("ola")

        #click on the publish
        comment_button = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[3]/div/form/button")
        comment_button.click()
