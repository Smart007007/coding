#coding='utf-8'
#定义浏览器实例,
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from testPage import config
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 定义浏览器对象
chrome_options = Options()
Options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
#打开浏览器
driver.get(config.qqemail_url)
driver.implicitly_wait(2)
#登录qq,并打印结果
config.qqMailLogin(driver,"321706056","skd..@123")


mobile=driver.find_element(By.LINK_TEXT,"手机版").click()
#定位手机版点击进入

#转移句柄到新页面
handles=driver.window_handles
driver.switch_to.window(handles[1])
#滚动条到最后一行
js="window.scrollTo(0,10000)"
driver.execute_script(js)
sleep(3)
#关闭当前窗口
driver.close()
#将句柄转移至第一个页面
driver.switch_to.window(handles[0])

#再次定位iframe

#再次切换至frame下
#再次定位用户名密码、登录按钮
#再次登录、登录失败
config.qqMailLogin(driver,"321776056","skd..@123")

# #定位iframe元素
# ifram=driver.find_element_by_css_selector("[id^='login_frame']")
# #转移至frame
# driver.switch_to.frame(ifram)
#
# #账号、密码、登录操作
# uname=driver.find_element_by_xpath("//form[@id='loginform']/div[1]/div[1]/input")
# password=driver.find_element_by_xpath("//form[@id='loginform']/div[2]/div[1]/input")
# dl=driver.find_element_by_xpath("//form[@id='loginform']/div[4]/a/input")
#
# #登录失败，获取登录错误信息
# uname.clear()
# uname.send_keys("321706056")
# password.clear()
# password.send_keys("skd..@123")
#
# dl.click()
# sleep(5)
# errtext=driver.find_element(By.CSS_SELECTOR,"#err_m").text
# print("登录失败，信息是： %s"%errtext)
#关闭浏览器
driver.quit()



























