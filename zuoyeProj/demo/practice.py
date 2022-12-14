#coding="utf-8"
from common import config


class BasePage(object):
    def __init__(self,driver,url=config.base_url):
        self.driver=driver
        self.url=url

    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
             print("异常发生，页面打开失败，： %s\n: %s"%(e,self.url))


