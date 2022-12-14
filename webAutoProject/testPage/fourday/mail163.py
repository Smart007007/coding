#coding='utf-8'
#定义浏览器实例,
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from testPage import config
# 定义浏览器对象
# #打开浏览器
driver=config.getDriver(config.email_163_url)
driver.implicitly_wait(1)
#定位iframe元素
# ifram=driver.find_element_by_css_selector("[id^='x-URS-iframe']")
ifram=config.findElement(driver,By.CSS_SELECTOR,"[id^='x-URS-iframe']")

#将光标转移至小页面(frame)下    ifram上接主框架，下接独立小框架
driver.switch_to.frame(ifram)

#定位账号密码登录
# uname=driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input")
# password=driver.find_element_by_css_selector(".j-inputtext.dlpwd")
# dl=driver.find_element_by_css_selector(".u-loginbtn.btncolor.tabfocus.btndisabled")
uname=config.findElement(driver,By.XPATH,"//div[@id='account-box']/div[2]/input")
password=config.findElement(driver,By.CSS_SELECTOR,".j-inputtext.dlpwd")
dl=config.findElement(driver,By.CSS_SELECTOR,".u-loginbtn.btncolor.tabfocus.btndisabled")

# uname.send_keys("skd139@007")
config.doInputvalue(uname,"skd139@007")
# password.send_keys("1234567")
config.doInputvalue(password,"1234567")

#点击登录按钮
# dl.cli
config.doClick(dl)

#截图、查看当前页面信息
config.dophoto(driver,"1")

driver.implicitly_wait(1)

#打印当前信息
config.printCurrinfo(driver)

#回到主页面 default_content默认回到主页面
driver.switch_to.default_content()

#再打印一次
config.printCurrinfo(driver)
driver.implicitly_wait(1)

# vip=driver.find_element_by_link_text("会员")
vip=config.findElement(driver,By.LINK_TEXT,"会员")
# vip.click()
config.doClick(vip)

#句柄转移
handlers=driver.window_handles
driver.switch_to.window(handlers[-1])

# sleep(3)
driver.implicitly_wait(3)

#截图、查看当前页面信息
config.dophoto(driver,"2")

#关闭浏览器
driver.quit()


