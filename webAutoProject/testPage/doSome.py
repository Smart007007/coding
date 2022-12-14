# coding='utf-8'
#控件元素的常用操作
from time import sleep
from selenium import webdriver
import config
# #定义浏览器对象
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
Options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)

#打开页面
driver.get(config.url)
driver.maximize_window()
sleep(2)

#定位输入框
# inpt=driver.find_element_by_css_selector("#kw")
# sleep(3)

# #输入内容
# inpt.send_keys("python")
# sleep(3)
# #模拟回车键
# inpt.submit()
# sleep(3)
#
# # #获取大小
# # print(inpt.size)
# # #判断是否可见
# # print("输入框是否可见:",inpt.is_displayed())
# # #判断是否可用
# # print("输入框是否可用:",inpt.is_enabled())
# #
# # #判断是否选中
# # print("输入框是否选择:",inpt.is_selected())
# #
# # #输入内容
# # inpt.send_keys("python")
# # sleep(3)
# #
# # #清除文本内容
# # inpt.clear()
# # sleep(3)
#
#
# # #定位右上角的登录，并点击
# # logA=driver.find_element_by_css_selector("#u1>a")
# # logA.click()
# # sleep(3)
# # #定位登录框中的登录按钮，并点击
# # logbt=driver.find_element_by_id("TANGRAM__PSP_11__submit")
# # logbt.click()
# # print(logbt.get_attribute("class"))
# # print(logbt.get_attribute("id"))
# # sleep(2)
# #
# # #定位错误的提示信息
# # error=driver.find_element_by_id("TANGRAM__PSP_11__error")
# # #获取错误的提示信息，并打印
# # print("错误信息是: ",error.text)
# # # print("错误信息是:%s'% error.text'")
# # sleep(3)

#关闭浏览器

#鼠标操作类
# action=ActionChains(driver)
#
# #定位更多超链接
# ax=driver.find_element_by_link_text("更多")

#使用鼠标对象做悬停操作
# action.move_to_element(ax)
# sleep(2)
#针对更多进行右击操作
# action.context_click(ax)
# action.perform()
# sleep(3)
#
# #d定位”换一换“元素，进行双击操作
# hh=driver.find_element_by_xpath("//span[text()='换一换']")
# action.double_click(hh)

#定位百度输入框下面的超链接,然后进行拖拽
# aa=driver.find_element_by_partial_link_text("新进展")
# #使用鼠标对象要用拖拽方法
# action.drag_and_drop(aa,ax)

# #去执行鼠标的操作
# action.perform()

#弹出框
#定位一个弹出框按钮
# bt1=driver.find_element_by_id("1")
# bt2=driver.find_element_by_id("2")
bt3=driver.find_element_by_css_selector("[value='确认弹窗按钮']")
bt3.click()
sleep(2)

#操作弹出框    定位转移到弹窗
alert=driver.switch_to.alert

#第一种弹窗,需要填写内容
# #获取弹窗的文本信息，并打印     为什么没有括号：他是一个属性，就是变量，直接类.什么什么 不需要括号
# alerText=alert.text
# print("弹窗中的文本内容是: %s"%alText)
# #向输入框中输入内容
# alert.send_keys("1")
# #点击弹窗中的取消按钮
# # alert.dissmiss()
# #点击弹窗中的确定按钮
# alert.accept()
# sleep(5)
#第二种弹窗,仅仅是提示信息，不需要做选择
# info=alert.text
# print("第二个弹窗的文本值是: %s"%info)

#第三种弹窗
info=alert.text
print("第三个弹窗文本值是: %s"%info)

#点击alert的确定按钮
alert.accept()

#定位页面中的结果
result=driver.find_element_by_css_selector("#textSpan>font")
print("弹窗关闭后，页面中的结果是: %s"%result.text)




sleep(3)
driver.quit()











