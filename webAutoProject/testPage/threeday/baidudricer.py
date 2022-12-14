#coding='utf-8'
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
#定位到登录按钮
dw=driver.find_element_by_id("s-top-loginbtn")
dw.click()
sleep(3)
#登录页面，定位百度协议，
dwxy=driver.find_element_by_link_text("百度用户协议")
dwxy.click()
sleep(3)
#
# #打印出当前页面的标题，句柄，url
handlers=driver.window_handles
onehandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口的标题是: %s,\n当前窗口url是: %s"%(title,cur_URL))
print("当前窗口的句柄是: %s"%onehandler)
print("当前所有窗口的句柄有哪些: %s"% str(handlers))

#转移句柄到百度协议下----获取最后一个元素的值
# driver.switch_to.window(handlers[-1])

#打印出转移后的标题，句柄，url
twohandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("移交句柄后，当前窗口的句柄是：%s,\n转移后的窗口的URL是: %s,\n转移后的窗口标题是: %s"%(twohandler,cur_URL,title))


#定位”百度用户协议“元素，并打印文本值
wb=driver.find_element_by_xpath("/html/body/div[2]/div[1]")
print("打印的文本值是: %s"%wb)
#再次切换到百度一下页面


#关闭当前窗口


#退出浏览器