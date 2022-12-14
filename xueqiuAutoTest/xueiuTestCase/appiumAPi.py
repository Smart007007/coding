import time
from appium import webdriver
_AppPackage = 'com.xueqiu.android'
_AppWaitActivity = '.view.WelcomeActivityAlias'
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
# caps['deviceName'] = '127.0.0.1:62001'
caps['uuid']='127.0.0.1:62001'
caps['appPackage'] = _AppPackage
caps['appActivity'] = _AppWaitActivity
caps['noReset'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
driver.implicitly_wait(30)
driver.close_app()
print(driver.is_app_installed(_AppPackage))
driver.remove_app(_AppPackage)
time.sleep(5)
# 安装app
driver.install_app("C:\\Users\\007\\Desktop\\xueqiu.apk")
time.sleep(2)
# 打开指定页面
driver.start_activity(_AppPackage,_AppWaitActivity)
time.sleep(5)
# 置后台
driver.background_app(5)
time.sleep(2)
driver.reset()
# 操作键码表
driver.press_keycode(26)
# 手势类操作，滑动、长按、拖拽
from appium.webdriver.common.touch_action import TouchAction
# 按压控件element或坐标点二选一即可不能填写两个；release()结束动作，释放按压指针；perform()执行
TouchAction(driver).press(element/坐标点[x,y]).release().perform()
# 长按、先执行、后释放
TouchAction(driver).long_press(element).perform().release()
# 点击,注意：语法列表套元组-[(x,y)]第一种：内置tap函数、第二种：使用TouchAction类
driver.tap([(100,200)])
TouchAction(driver).tap(element=).perform().release()
# 暂停,单位是毫秒
TouchAction(driver).wait(2000)
# 移动,element目标位置元素
TouchAction(driver).move_to(element).perform().release()
TouchAction(driver).long_press().move_to().perform().release()
# 滑动
driver.swipe(x1,y1,x2,y2,times)
# 收起键盘
driver.hide_keyboard()
# 摇一摇
driver.shake()
# 滚动，从a元素到b元素
driver.scroll(A_element,B_element)
driver.flick(x1,y1,x2,y2)
# 放大缩小
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
action1=TouchAction(driver)
action2=TouchAction(driver)
zoom=MultiAction(driver)
action1.press(x1,y1).wait(1000).move_to(x1,y1).wait(1000)
action2.press(x1,y1).wait(1000).move_to(x1,y1).wait(1000)
zoom.add(action1,action2)
# 获取屏幕分辨率(宽、高)
x=driver.get_window_size()['width']
y=driver.get_window_size()['height']
# 缩放-点到点
driver.swipe(0.8*x,0.5*y,0.2*x,0.1*y,2000)
# 网络
driver.set_network_connection(4)
# 通知栏
driver.open_notifications()
# 修改经纬度
driver.set_location(longitude=21,latitude=18,altitude=None)
# is_enabled 编辑、is_selected选择、is_displayed可见
driver.find_element().is_selected()
driver.find_element().is_displayed()
assert driver.find_element().is_enabled() is True
from appium.webdriver.common.mobileby import MobileBy
driver.find_element(MobileBy.ID)
driver.switch_to.context('webview页面')




