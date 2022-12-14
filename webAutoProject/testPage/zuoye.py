# coding='utf-8'

from time import sleep

import click as click
from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://139.199.0.102/dashboard')
sleep(3)
# driver.maximize_window()
# sleep(1)
i = driver.find_element_by_xpath("//input[(@placeholder='请输入手机号码')]")
i.send_keys("13986128128")
sleep(3)
# 通过xpath：相对路径，模糊匹配，部分值-----密码输入框定位
i = driver.find_element_by_xpath("//form//input[@type='password']")
i.send_keys("121121")
sleep(3)

#记住密码校验
# i1=driver.find_element_by_xpath("//span[text()='记住密码']")
# i1.click()
# sleep(2)
# i2=driver.find_element_by_xpath("//*[@class='ant-checkbox-input']")
# i2.click()
# sleep(2)

#忘记密码定位
# i3=driver.find_element_by_class_name('forgot.ng-tns-c1-0')
# i3.click()
# sleep(1)
#
# #返回
# driver.back()
# sleep(1)

# #打印出当前页面的标题，句柄，url
handlers=driver.window_handles
onehandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口的标题是: %s,\n当前窗口url是: %s"%(title,cur_URL))
print("当前窗口的句柄是: %s"%onehandler)
print("当前所有窗口的句柄有哪些: %s"% str(handlers))


#转移句柄到百度协议下
# driver.switch_to.window(handlers[-1])

#打印出转移后的标题，句柄，url
twohandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("移交句柄后，当前窗口的句柄是：%s,\n转移后的窗口的URL是: %s,\n转移后的窗口标题是: %s"%(twohandler,cur_URL,title))


#立即登录
i4=driver.find_element_by_xpath("//button[@type='submit']")
i4.click()
sleep(1)

# i5=driver.find_element_by_xpath("//div[@class='flex_H_Center']")
# i5.click()
# sleep(1)