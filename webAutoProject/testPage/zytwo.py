from time import sleep
from selenium import webdriver
from testPage import config
from time import sleep
from selenium import webdriver
# #定义浏览器对象
from selenium.webdriver.chrome.options import Options
#浏览器案例并打开页面
driver=config.getDriver(config.email_163_url)
driver.implicitly_wait(1)
#定位第二按钮，点击该按钮
but2=driver.find_element_by_id("2")
but2.click()
#移交权限，并创建弹窗对象
alert=driver.switch_to.alert

#开始操作弹窗~~~~~~~~~~
#获取弹窗文本
alertText=alert.text
print("我是第二额弹窗，我的文本信息是: %s"% alertText)

#操作弹窗按钮，确定
alert.accept()
#操作弹窗结束~~~~~~

#开始操作浏览器，定位第三个按钮
hello=driver.find_element_by_xpath("//div/input[3]")
sleep(3)
text=hello.get_attribute("value")
print("我现在在浏览器页面，标题内容是: %s" % text)