#coding='utf-8'
#定义浏览器实例,
from selenium.webdriver import ActionChains
from testPage import config
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# #定义浏览器对象
chrome_options = Options()
Options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
#浏览器案例并打开雷小锋登录页面
driver.get(config.url)
sleep(3)
jb=driver.window_handles
#获取当前窗口window_handle
onehandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口的句柄是: %s,\n当前窗口url是: %s"%(onehandler,cur_URL))
print("当前窗口的标题是: %s"%title)
#登录
i = driver.find_element_by_xpath("//input[(@placeholder='请输入手机号码')]")
i.send_keys("13986128128")
sleep(3)
i = driver.find_element_by_xpath("//form//input[@type='password']")
i.send_keys("121121")
sleep(3)
#定位+点击登录
i4=driver.find_element_by_xpath("//button[@type='submit']")
i4.click()
sleep(3)
#移交句柄至工作台---切换之前的（jb）
driver.switch_to.window(jb[-1])
#打印出当前页面的标题，句柄，url
twohandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口的句柄是: %s,\n当前窗口url是: %s"%(twohandler,cur_URL))
print("当前窗口的标题是: %s"%title)

#判断登陆是否成功
if title=='工作台 - 雷小锋':
    print('恭喜您登陆成功!')
else:
    print('登陆失败!')
sleep(2)
#定位头像
ax=driver.find_element_by_xpath('//layout-header/div[1]/div[2]/div[5]/img')
#使用鼠标对象做悬停操作
action=ActionChains(driver)
#悬浮头像
action.move_to_element(ax)
action.perform()
#定位退出+点击
tc=driver.find_element_by_xpath('//layout-header/div[1]/div[2]/div[5]/div[2]/div[4]')
tc.click()
sleep(3)
#定位弹窗+点击确定
tc1=driver.find_element_by_class_name("ant-btn.ng-star-inserted.ant-btn-primary").click()
sleep(3)
#打印出当前页面的标题，句柄，url
threehandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print('退出登录后当前页面标题是： %s,\n退出登录后当前页面句柄是： %s,\n退出登录后当前页面url是： %s'%(title,threehandler,cur_URL))
sleep(3)
#关闭浏览器
driver.quit()