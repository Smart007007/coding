# coding="utf-8"
# #定义类A临时补充继承类
# class  A():
#     def a1(self):
#      print(1+2)
#     def  a2(self):
#         print(1*2)
#     def  __a3(self):
#         print("nihai")
# #定义类B，同时继承类A
# class B(A):
#     def b1(self):
#         print(1-2)
#
# # 仅仅在本py文件中执行的代码
# # __name__表示任何一个py模块下都有的一个私有变量
# # 本模块(py文件)下该__name__的值就等于__main__
# # 对外(py)时__name__的值是：该模块名称： basePage
# if __name__=="__main__":
#     bb=B()
#     bb.a2()
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common import config
from demo.pageObject.basePage import BasePage

if __name__=="__main__":
    driver=webdriver.Chrome()
# 百度
    llq=BasePage(driver,config.ba_url)
    llq.open()
    llq.driver.implicitly_wait(10)
    locater=(By.ID,"kw")
    llq.inputValue(locater,"python")
    llq.doPhoto("图一")
    llq.doClick((By.ID,"su"))
    sleep(3)
    llq.doPhoto("图二")
    ff=(By.CSS_SELECTOR,'.hint_PIwZX.c_font_2AD7M')
    llq.getElementValue(ff)
    sleep(3)

# 雷小锋
    lxf=BasePage(driver,config.xlf_url)
    lxf.open()
    lxf.driver.implicitly_wait(10)
    lxf.doPhoto("图三")
    ddw=(By.CSS_SELECTOR,'.forgot.ng-tns-c1-0')
    lxf.doClick(ddw)
    sleep(5)
    lxf.doPhoto("图四")
    dw=(By.XPATH,"/html/body/app-root/layout-passport/div[1]/div[1]/div[1]/div[1]")
    lxf.getElementValue(dw)
    sleep(3)
    lxf.driver.quit()
