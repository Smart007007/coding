import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
# from selenium.webdriver.common.by import By

from ApptestCase import param
des_caps={}
des_caps["platformName"]=param.AppActions.PlatformName
# print(str(os.popen("adb -s 127.0.0.1:62001 shell getprop ro.build.version.release")))
# des_caps["platformVersion"]=str(os.system("adb -s 127.0.0.1:62001 shell getprop ro.build.version.release"))
des_caps["platformVersion"]=param.AppActions.PlatformVersion
# print(type(param.AppActions.PlatformVersion))
des_caps["deviceName"]=param.AppActions.DeviceName
des_caps["noReset"]=param.AppActions.NoReset
des_caps["app"]=param.AppActions.App
des_caps["appPackage"]=param.AppActions.AppPackage
des_caps["appWaitActivity"]=param.AppActions.AppWaitActivity
des_caps["unicodeKeyboard"]=param.AppActions.UnicodeKeyboard
des_caps["resetKeyboard"]=param.AppActions.ResetKeyboard
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=des_caps)
driver.implicitly_wait(20)
# driver.find_element(MobileBy.ID,"home_search").click()
# driver.find_element(MobileBy.ID,"post_status").click()
# driver.find_element(By.ACCESSIBILITY_ID,"content-desc值")
"""
ANDROID_UIAUTOMATOR 定位方法是Android原生定位方法，和xpath有点类似，比xpath更加好用；
支持元素的全部属性进行定位，使用函数uiSelector
表达式：new UiSelector(). 函数名称("定位表达式")
        实例化一个uiSeletor对象，通过实例对象调用对应的方法，每个方法都会返回实例对象
函数：
1、id方法
resourceId("id值")
resourceIdMatches("id部分值")  id的正则表达式

2、text文本方法
text("文本值")
textContions("文本部分")    文本包含
textStartWith("文本头部")   文本头部
textMatches("文本部分值")    文本正则表达式

3、描述方法
description("desc") 描述
descriptionContains("desc") 描述包含
descriptionStartWith("desc") 描述开头
descriptionMatches("desc")  描述正则表达式
   
4、class方法
className("class值")   类名

5、索引、实例方法
index("index值")   编号
instance("")    索引

6、特殊属性
checked("布尔值")  选择属性
checkable("布尔值")  点击属性
longClickable("布尔值")  长按属性

7、多属性组合
示例：
new UiSelector().resourceId("id值").text("text文本")
new UiSelector().className("class值").text("布尔值")

"""
driver.find_element(By.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"交易\")").click()












