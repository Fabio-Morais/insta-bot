from selenium import webdriver
from time import sleep
import logging

from comment import comment

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger = logging.getLogger('scraping')# singleton pattern
logger.info('Start....')


browser = webdriver.Chrome(executable_path="C:/Users/fabio/Documents/chromedriver")
browser.implicitly_wait(5)
browser.get("http://instagram.com")
login_link = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
login_link.click()

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("fabiouds12345")
password_input.send_keys("catarina12345")

#click on login button
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

#click on Not Now (dont save login info)
login_button = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
login_button.click()

#click on Not Now (turn on notifications)
login_button = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
login_button.click()

browser.get("https://www.instagram.com/p/CCrOLnpnL7CjZc3RFyu3L13MI6M_QxAlVy-7Dk0/")

#comment
com = comment(browser)
com.comment_something()

