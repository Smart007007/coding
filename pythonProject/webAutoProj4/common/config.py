# coding="utf-8"
# 所有的配置文件的信息
import os
import time

from selenium import webdriver

ba_url="http://baidu.com"
xlf_url="http://139.199.0.102/dashboard"
# def getDriver(url):
#     try:
#         driver=webdriver.Chrome()
#     except Exception as e:
#         print("发生异常，浏览器实例化失败！\n错误信息： %s"%e)
#     else:
#         print("未发生异常，浏览器实例化成功！ ")
#
#     try:
#         #打开页面
#         driver.get(url)
#     except Exception as e:
#         print("页面打开失败： %s\n错误信息是： %s"%(url,e))
#     else:
#         print("未发生异常，页面被成功打开： %s"%url)
#         # sleep(3)
#         driver.implicitly_wait(3)
#         return driver


# 定义当前时间
cur_time=time.strftime("%Y_%m_%d %H_%M_%S")

# 当前日期
cur_date=time.strftime("%Y_%m_%d")

# 基本的页面地址
base_url="http://139.199.0.102/passport/login"

# 项目路径
base_path=r"D:\PythonCoding\pythonProject\webAutoProj4\\"

# 截图路径
# photo_path=base_path+"/data/photos/"
photo_path=os.path.join(base_path,r"data\photos\\")

# log路径
# log_path=base_path+"/data/logs/"
log_path=os.path.join(base_path,r"data\logs\\")

#数据路径
data_path=os.path.join(base_path,r'data\testDatas\\')

#测试用例的路径
test_path=os.path.join(base_path,r"demo\testCase\\")

# 测试报告路径
report_path=os.path.join(base_path,r"data\reports\\")