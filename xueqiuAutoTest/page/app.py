from appium import webdriver
from page.BasePage import BasePage
from page.main import Main
class APP(BasePage):
    def star(self):
        _AppPackage='com.xueqiu.android'
        _AppWaitActivity='.view.WelcomeActivityAlias'
        if self._driver is None:
            # caps={}
            # caps['platformName']='Android'
            # caps['platformVersion']='7.1.2'
            # caps['deviceName']='127.0.0.1:62001'
            # caps['appPackage']=_AppPackage
            # caps['appActivity']=_AppWaitActivity
            # caps['noReset']=True
            # self._driver=webdriver.Remote("http//127.0.0.1:4723/wd/hub",caps)
            # self._driver.implicitly_wait(30)
            caps = {}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '7.1.2'
            caps['deviceName'] = '127.0.0.1:62001'

            caps['appPackage'] = _AppPackage
            caps['appActivity'] = _AppWaitActivity
            caps['noReset'] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(30)
        else:
            # stat_activity仅供Android
            self._driver.start_activity(_AppPackage,_AppWaitActivity)
        return self
    def main(self):
        return Main(self._driver)