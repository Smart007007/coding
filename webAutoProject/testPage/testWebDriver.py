#coding='utf-8'
#测试浏览器去驱动
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from testPage import config

# options = webdriver.ChromeOptions()
# # options设置chrome位置
# options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
# # 配置到实例
# #定义浏览器驱动
# driver = webdriver.Chrome(chrome_options=options)

#打开页面
driver=config.getDriver(config.ba_url)
#最大化
driver.maximize_window()
sleep(1)

# 最小化
driver.minimize_window()
sleep(3)

# 打开新页面
driver.get("http://www.w3school.com.cn")
sleep(1)

# 刷新命令
driver.refresh()
sleep(3)

#上一页
driver.back()
sleep(1)

#下一页
driver.forward()
sleep(3)

#关闭窗口,关闭当前页面
driver.close()
sleep(3)



# 退出浏览器
#

#元素定位
#通过定位百度一下首页的输入框
# inp=driver.find_element_by_id("kw")

#通过name定位百度一下首页的输入框
# inp=driver.find_element_by_name("wd")

#通过class_name定位百度一下首页输入框
# inp=driver.find_element_by_class_name("s_ipt")

#通过标签定位页面元素，tag_name不唯一，一般不使用   elements加s表示获取多个--表示返回列表list
# inp=driver.find_elements_by_tag_name("input")

#通过xpath-绝对路径定位输入框
# inp=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[1]/div[1]/form/span[1]/input")

#通过xpath:相对路径定位输入框   父子类型
# inp=driver.find_element_by_xpath("//form/span[1]/input")

#通过xpath：相对路径定位输入框。相对加绝对    父子类型
# inp=driver.find_element_by_xpath("//form//input[@id='kw']")

#通过xpath：相对路径//，属性
# inp=driver.find_element_by_xpath("//input[@id='kw']")

#第二天内容：通过css选择器定位元素,id用#号                 要么id要么class 其余全是name
# inp=driver.find_element_by_css_selector("#kw")
#第二天内容：通过css选择器定位元素class：用点'.',也就是类名
# inp=driver.find_element_by_css_selector(".s_ipt")
#第二天内容：通过css选择器定位元素，name
inp=driver.find_element_by_css_selector("[name='wd']")

#向文本框中输入内容
# inp.send_keys("python")
# sleep(3)
#百度一下：id和class、name
# a=driver.find_element_by_css_selector("#su")
# a=driver.find_element_by_css_selector(".bg.s_btn")
# a=driver.find_element_by_css_selector("[type='submit']")
# a=driver.find_element_by_css_selector("[value='百度一下']")
# a.click()
# sleep(3)



#通过xpath：相对路径，模糊匹配，部分值，百度一下按钮
# but=driver.find_element_by_xpath("//input[contains(@class,'s_btn')]")

# but=driver.find_element_by_id("su")
# but=driver.find_element_by_class_name("bg.s_btn")
# but=driver.find_element_by_xpath("//form//input[@id='su']")
# but=driver.find_element_by_xpath("//form/span[2]/input")
# but=driver.find_element_by_xpath("//input[@type='submit']")
# but=driver.find_element_by_xpath("//*[@type='submit' and @value='百度一下']")

#分别通过id、class、xpath(绝对、相对+绝对、相对（属性、分别通过type、value）)
# but.click()

#通过text值，text()方法定位元素     方法后需要加括号   通过某个值
# setting=driver.find_element_by_xpath("//span[text()='设置']")
# setting=driver.find_element_by_xpath("//*[text()='设置']")
# setting.click()

#通过超链接定位元素     a标签或某某标签代表超链接
# a1=driver.find_element_by_link_text("新闻")
# #通过超链接部分信息定位元素
# a2=driver.find_element_by_partial_link_text("中国空天变化")
# a2.click()
# sleep(3)
#
# #关闭当前窗口
# driver.close()

#通过css选择器定位元素：父子    id用#号   name用$表示   括号里面的是f12之后所在位置减一
# login=driver.find_element_by_css_selector("#u>a:nth-child(3)")
# login.click()

#通过css选择器，定位元素，模糊匹配:包含前半部分^^^
# login=driver.find_element_by_css_selector("a[class^='s-top-login-btn']")
#通过css选择器，定位元素，模糊匹配:包含后半部分$$$
# login=driver.find_element_by_css_selector("a[id$='loginbtn']")
#通过css选择器，定位元素，模糊匹配:包含部分****
# login=driver.find_element_by_css_selector("a[class*='c-btn-mini']")
# login=driver.find_element_by_css_selector("a[class^='s-top-login-btn']")
login=driver.find_element(By.CSS_SELECTOR,"a[class^='s-top-login-btn']")
login.click()
sleep(3)

driver.quit()

#定位元素