# coding="utf-8"
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.doExcel import DoExcel
from demo.pageObject.basePage import BasePage, testData


# 在该文件种定义用户名、密码、登录按钮、错误信息。定义登录方法
class LoginPage(BasePage):

    #定义用户名
    # unameLocator=(By.CSS_SELECTOR,'[formcontrolname="userName"]')
    unameLocator=(By.CSS_SELECTOR,testData.readExcel(1,4))

    # updownLocator=(By.CSS_SELECTOR,'[formcontrolname="password"]')
    updownLocator=(By.CSS_SELECTOR,testData.readExcel(2,4))
    #定义登录按钮
    # butLocator=(By.CSS_SELECTOR,"[type='submit']")
    butLocator=(By.XPATH,testData.readExcel(3,4))
    #定义错误信息，登录信息空的时候的错误信息
    # errorUname=(By.XPATH,'//form/nz-form-item[1]/nz-form-control/div/nz-form-explain/div')
    errorUname=(By.XPATH,testData.readExcel(4,4))
    # errorUpwd=(By.XPATH,' //form/nz-form-item[2]/nz-form-control/div/nz-form-explain/div')
    errorUpwd=(By.XPATH,testData.readExcel(5,4))

    #错误信息，登录信息失败时候的弹窗错误信息
    # errMesage=(By.CSS_SELECTOR,'.ant-modal-confirm-title>span')
    errMesage=(By.CSS_SELECTOR,testData.readExcel(6,4))
    #错误信息弹窗,弹窗中的确认按钮
    # errBut=(By.CSS_SELECTOR,'.ant-btn.ng-star-inserted.ant-btn-primary')
    errBut=(By.CSS_SELECTOR,testData.readExcel(7,4))

    #登录数据
    loginData=DoExcel(wk="testData.xlsx",st="loginData")
    lginDataList=[[int(loginData.readExcel(1,2)),int(loginData.readExcel(1,3))],#用户名正确、密码正确
                  [loginData.readExcel(2,2),loginData.readExcel(2,3)],#用户名空、密码空
                  [loginData.readExcel(3,2),int(loginData.readExcel(3,3))],#用户名空、密码非空
                  [int(loginData.readExcel(4,2)),loginData.readExcel(4,3)],#用户名非空、密码空
                  [int(loginData.readExcel(5,2)),int(loginData.readExcel(5,3))],#用户名错误、密码正确
                  [int(loginData.readExcel(6,2)),int(loginData.readExcel(6,3))],#用户名正确、密码错误
                  [int(loginData.readExcel(7,2)),int(loginData.readExcel(7,3))],#用户名错误、密码错误
                  [int(loginData.readExcel(8,2)),int(loginData.readExcel(8,3))],#用户名长度不够、密码正确
                  [int(loginData.readExcel(9,2)),int(loginData.readExcel(9,3))],#用户名长度超出（12），密码正确
                  [int(loginData.readExcel(10,2)),int(loginData.readExcel(10,3))],#用户名正确，密码长度不够
                  [int(loginData.readExcel(11,2)),int(loginData.readExcel(11,3))]]#用户名正确，密码过长

    #登录方法
    def loginFun(self,vname=lginDataList[0][0],vpwd=lginDataList[0][1]):
        #输入用户名
        self.inputValue(self.unameLocator,vname)
        #输入密码
        self.inputValue(self.updownLocator,vpwd)
        sleep(2)
        #点击登录按钮
        self.doClick(self.butLocator)
        sleep(1)
# 自测方法
if __name__=="__main__":
    driver=webdriver.Chrome()
    login=LoginPage(driver)
    login.open()

    login.loginFun()
    # 登录失败
    # login.loginFun("","")
    # # 获取错误信息的值，并打印
    # errorName=login.getElementValue(login.errorUname)
    # print(errorName)
    # errotPwd=login.getElementValue(login.errorUpwd)
    # print(errotPwd)
    # # #登录失败，值错误
    # login.loginFun("13986128128","121121")
    # # #获取弹窗错误信息，并打印
    # errMsg=login.getElementValue(login.errMesage)
    # print(errMsg)
    # #点击弹窗中的确定按钮
    # login.doClick(login.errBut)
    print("我的登录数据是",login.lginDataList)
