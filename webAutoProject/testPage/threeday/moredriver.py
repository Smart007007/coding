#coding='utf-8'
#多窗口切换

#定义浏览器实例,并打开页面:百度一下
from testPage import config
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# #定义浏览器对象
chrome_options = Options()
Options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
#浏览器案例并打开页面
driver.get(config.url)
#点击百度一下页面中的超链接：hao123
a123=driver.find_element_by_link_text("hao123")
a123.click()
sleep(3)

#关键性一步：移交句柄
handlers=driver.window_handles
onehandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口的标题是: %s,\n当前窗口url是: %s"%(title,cur_URL))
print("当前窗口的句柄是: %s"%onehandler)
print("当前所有窗口的句柄有哪些: %s"% str(handlers))

#句柄转移窗口切换
driver.switch_to.window(handlers[-1])
#获取当前句柄
twohandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("移交句柄后，当前窗口的句柄是：%s,\n转移后的窗口的URL是: %s,\n转移后的窗口标题是: %s"%(twohandler,cur_URL,title))

#操作hao123页面
driver.close()
sleep(3)

# #再次切换到最初页面
# driver.switch_to.window(onehandler)

driver.quit()



