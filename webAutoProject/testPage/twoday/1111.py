#coding='utf-8'
from selenium import webdriver
from testPage import config

# driver=webdriver.Chrome()
# driver.get(config.email_163_url)
driver=config.getDriver(config.email_163_url)