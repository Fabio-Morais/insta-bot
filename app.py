from selenium import webdriver
import logging

from automation import Automation

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')
logger = logging.getLogger('scraping')# singleton pattern
logger.info('Start....')


browser = webdriver.Chrome(executable_path="C:/Users/fabio/Documents/chromedriver")
browser.implicitly_wait(5)
browser.get("http://instagram.com")
com = Automation(browser)
com.login()
browser.get("https://www.instagram.com/p/CCrOLnpnL7CjZc3RFyu3L13MI6M_QxAlVy-7Dk0/")
#comment
com.like_post()

