#coding='utf-8'
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from testPage import config
from time import sleep
#浏览器案例并打开雷小锋登录页面
driver=config.getDriver(config.xlf_url)
driver.implicitly_wait(2)
#登录雷小峰项目
#打印出当前句柄、标题、url
# title1=driver.title
# cur_url=driver.current_url
# cur_handle=driver.current_window_handle
# print("登录前页面的标题是: %s,\n登录前页面的url是: %s,\n登录前页面的句柄是: %s"%(title1,cur_url,cur_handle))
config.printCurrinfo(driver)

#定位登录页面元素
# uname=driver.find_element_by_css_selector("[formcontrolname='userName']")
# upws=driver.find_element_by_css_selector("[formcontrolname='password']")
# loginBut=driver.find_element_by_xpath("//button[@type='submit']")
uname=config.findElement(driver,By.CSS_SELECTOR,"[formcontrolname='userName']")
upws=config.findElement(driver,By.CSS_SELECTOR,"[formcontrolname='password']")
loginBut=config.findElement(driver,By.XPATH,"//button[@type='submit']")
#填写用户名登录密码
uname.send_keys("13986128128")
upws.send_keys("121121")
#点击登录按钮
loginBut.click()
driver.implicitly_wait(2)
#登录成功后，判断是否成功
# logOK=driver.find_element_by_xpath("//div[@id='headerH']/div[2]/div[5]/div[1]/span[2]")
logOK=config.findElement(driver,By.XPATH,"//div[@id='headerH']/div[2]/div[5]/div[1]/span[2]")
print(logOK.text)
if logOK.text=='13986128128':
    print('该用户登录成功！！！')
    #打印当前页面标题、url、句柄
    # cur_title = driver.title
    # cur_url = driver.current_url
    # cur_handle = driver.current_window_handle
    # print('登录后页面的标题是： %s,\n登陆后的页面url是： %s,\n登陆后的句柄是 ：%s'%(cur_title,cur_url,cur_handle))
    config.printCurrinfo(driver)
    #通过右上角个人中心，退出登录
    # persioninfo=driver.find_element_by_xpath("//div[@id='headerH']/div[2]/div[5]/img")
    persioninfo=config.findElement(driver,By.XPATH,"//div[@id='headerH']/div[2]/div[5]/img")
    #悬浮该个人中心图标
    action=ActionChains(driver)

    action.move_to_element(persioninfo)
    action.perform()
    #定位退出登录按钮
    # logOut=driver.find_element_by_xpath("//div[text()='退出账号']")
    logOut=config.findElement(driver,By.XPATH,"//div[text()='退出账号']")
    logOut.click()
    sleep(3)
    # driver.implicitly_wait(2)
    #定位弹窗信息
    # logOut2=driver.find_element_by_css_selector(".ant-btn.ng-star-inserted.ant-btn-primary")
    logOut2=config.findElement(driver,By.CSS_SELECTOR,".ant-btn.ng-star-inserted.ant-btn-primary")
    logOut2.click()
    driver.implicitly_wait(2)

#若登录成功，
    #打印出当前标题、url、句柄
    #通过右上角个人中心，退出登录

#退出登录后打印出当前的标题、句柄、url
# cur_title = driver.title
# cur_url = driver.current_url
# cur_handle = driver.current_window_handle
# print('退出登录后页面的标题是： %s,\n退出登陆后的页面url是： %s,\n退出登陆后的句柄是 ：%s'%(cur_title,cur_url,cur_handle))
config.printCurrinfo(driver)

driver.quit()









