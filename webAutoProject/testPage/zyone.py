from time import sleep
from selenium import webdriver
import config
# #定义浏览器对象
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
Options.binary_location = r"C:\Users\007\AppData\Local\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=chrome_options)

driver.get(config.url)
driver.maximize_window()


#第一个窗口按钮处理页面

#定义浏览器实例
driver.get(config.url)

#定位第一个按钮
but1=driver.find_element_by_id("1")
#点击第一个按钮
but1.click()

#将光标移交到弹窗,定义弹窗对象
alert=driver.switch_to.alert

#操作弹窗，===================弹窗开始
#获取文本
ix="ONE"
alerText=alert.text
#输出内容
alert.send_keys("1")
sleep(3)
ipt=input("请选择操作按钮：1表示选择确定，2表示选择取消：")

if ipt=="1":
    #点击按钮（确定）
    alert.accept()
else:
    #点击取消按钮
    alert.dismiss()

#===============弹窗结束
#操作浏览器，判断结束
result=driver.find_element_by_css_selector("#textSpan>font")

reText=result.text
ret1="强哥是真聪明啊"
ret2="左哥是真笨啊"

# if reText==[ret1] or reText==[ret2]:

if reText in (ret1,ret2):
    print("该用户点击的是确定按钮!,输入了内容")
elif ix!='确定':
    print("该用户点击了确定按钮，但是未输入内容")
else:
    print("该用户点击的是取消按钮!")

sleep(3)
driver.quit()