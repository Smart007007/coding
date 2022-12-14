#coding='utf-8'
#模拟鼠标操作
from selenium.webdriver import ActionChains

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
#定义鼠标对象
action=ActionChains(driver)

#操作鼠标：悬停
#定位悬停元素
seting=driver.find_element_by_xpath("//span[text()='设置']")
action.move_to_element(seting)
action.perform()
sleep(3)

#操作鼠标：右击
#定位右击的那个元素
action.context_click(seting)
action.perform()
sleep(3)

#操作鼠标：拖拽(将元素1拖拽到元素2)
#定位元素1.元素2
a1=driver.find_element_by_link_text("更多")
a2=driver.find_element_by_xpath("//span[contains(text(),'共创光明未来')]")

action.drag_and_drop(a2,a1)
action.perform()
sleep(3)

#操作鼠标：双击
#定位需要双击的那个元素
hh=driver.find_element_by_css_selector("#hotsearch-refresh-btn>span")
action.double_click(hh)
action.perform()
sleep(3)


driver.quit()




