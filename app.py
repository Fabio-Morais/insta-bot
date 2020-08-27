from selenium import webdriver
import logging

from automation import Automation
from import_people_names import ImportPeopleNames

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')# singleton pattern
logger.info('Start....')


browser = webdriver.Chrome(executable_path="C:/Users/fabio/Documents/chromedriver")
browser.implicitly_wait(5)
browser.get("http://instagram.com")
com = Automation(browser)
com.login()
browser.get("https://www.instagram.com/wuant/")
aux = ImportPeopleNames(browser)
aux.get_names(100)
#browser.execute_script("window.history.go(-1)") -> volta para trás
#comment
#com.follow()


# indentifica r e seguir
