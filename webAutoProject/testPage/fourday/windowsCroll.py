#coding='utf-8'
#页面滚动
#定义浏览器
#定义浏览器实例,
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from testPage import config
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# #定义浏览器对象
chrome_options = Options()
Options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
#打开百度浏览器
driver.get(config.getDriver(config.ba_url))
driver.implicitly_wait(2)
#定义右上角登录超连接
# dl=driver.find_element_by_css_selector(".s-top-login-btn.c-btn.c-btn-primary.c-btn-mini.lb")
dl=config.findElement(driver,By.CSS_SELECTOR,".s-top-login-btn.c-btn.c-btn-primary.c-btn-mini.lb")
#传值locaterA
locaterA=(By.CSS_SELECTOR,".s-top-login-btn.c-btn.c-btn-primary.c-btn-mini.lb")
#1116改定位方式--locater————————隐式等待只关注用得着的、显示等待    定位每一个元素
#显示等待、既定位元素又做判断，是否可见 如果可见，返回该元素。如果不可见，异常输出 timeout
dl=WebDriverWait(driver,5,0.1).until(EC.visibility_of_element_located(locaterA))
#显示等待，仅判断元素是否存在  异常是报的是没有这样的元素
# dl=WebDriverWait(driver,5,0.1).until(EC.visibility_of(dl))

#显示等待，元素出现(两件事情：定位并判断)
# dl=WebDriverWait(driver,5,0.1).until(EC.presence_of_element_located(locaterA))

#判断右上角登录按钮的文本值是否与预期的一致，预期值是：登录，做两件事情，既定位、又做判断，如果一致返回true
result=WebDriverWait(driver,5,0.1).until(EC.text_to_be_present_in_element(locaterA,"登录"))

#百度一下按钮的定位方式
bd_locator=(By.CSS_SELECTOR,"#su")
#判断按钮的value属性是否与预期的一致：预期的值是百度一下，做两件事情，既定位、又做判断，如果一致返回true
result2=WebDriverWait(driver,5,0.1).until(EC.text_to_be_present_in_element_value(bd_locator,"百度一下"))
print("百度按钮的value值是否正确： %s"%result2)

if result==True:
    print("登录按钮的文本值是否正确: %s"%result)
    dl.click()

# sleep(3)
driver.implicitly_wait(2)
#登陆页面定义""百度用户协议
# yhxy=driver.find_element_by_partial_link_text("用户协议")
yhxy=config.findElement(driver,By.PARTIAL_LINK_TEXT,"用户协议")
#打印当前标题、句柄、url
config.printCurrinfo(driver)

#点击超链接：百度用户协议
yhxy.click()
driver.implicitly_wait(2)
#移交句柄
jb=driver.window_handles
driver.switch_to.window(jb[1])
#打印当前标题、句柄、url
config.printCurrinfo(driver)

#获取当前title
# title=driver.title
sjtitle="用户协议"
#等待16日新学
# result=WebDriverWait(driver,5,0.1).until(EC.title_is(sjtitle))
result=WebDriverWait(driver,5,0.1).until(EC.title_contains(sjtitle))
print(result)

#操作滚动条
#定义js字符串
js="window.scrollTo(0,5000)"
#执行js脚本
driver.execute_script(js)
driver.implicitly_wait(2)
#关闭当前页面
driver.close()
driver.implicitly_wait(2)
#退出浏览器
driver.quit()









