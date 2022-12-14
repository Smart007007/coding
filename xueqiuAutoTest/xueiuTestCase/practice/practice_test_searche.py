import time
from appium import webdriver
_AppPackage='com.xueqiu.android'
_AppWaitActivity='.view.WelcmeActivityAlias'
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
# caps['deviceName'] = '127.0.0.1:62001'
caps['uuid']='127.0.0.1:62001'
caps['appPackage'] = _AppPackage
caps['appActivity'] = _AppWaitActivity
caps['noReset'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
driver.implicitly_wait(30)

driver.close_app()
print(driver.is_app_installed(_AppPackage))
driver.remove_app(_AppPackage)