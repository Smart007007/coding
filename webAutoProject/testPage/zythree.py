#coding='utf-8'
#第二个弹窗按钮处理页面
from testPage import config
from time import sleep
from selenium import webdriver

# #定义浏览器对象
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
Options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)
#浏览器案例并打开页面
driver.get(config.url)
#定位第三个按钮
but3=driver.find_element_by_xpath("//body/div[1]/input[3]")
#点击按钮
but3.click()
sleep(3)
#弹出弹窗,光标移交到弹窗上,并生成弹窗实例
alert=driver.switch_to.alert
#获取弹窗文本
alertText=alert.text
print("我是第三个弹窗，我的文本信息是: %s"% alertText)
#点击按钮,确定
alert.accept()
#弹窗操作结束~~~~~~~~~

#操作浏览器,并做判断,点击了哪个按钮
result=driver.find_element_by_css_selector("#textSpan>font")
rut1="您为何如此自信？"
rut2="您为何如此谦虚？"

if result.text==rut1:
    print("你点击的是确定按钮")
else:
    print("您点击的是取消按钮")




