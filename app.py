import datetime

import datetime as datetime
from selenium import webdriver
import logging

from automation import Automation
from fake_accounts.fake_account import FakeAccount
from import_people_names import ImportPeopleNames
from script_files.json_file import JsonFile

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')# singleton pattern
logger.info('Start....')


browser = webdriver.Chrome(executable_path="C:/Users/fabio/Documents/chromedriver")
browser.implicitly_wait(5)
x = FakeAccount(browser)
x.create_email()

#browser.execute_script("window.history.go(-1)") -> volta para trás
#comment
#com.follow()
# indentifica r e seguir
