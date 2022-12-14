import logging
import unittest
from time import sleep

from common.doLog import Logger
# coding="utf-8"
# 登录页面测试用例类
from demo.testCase.baseUnitest import BaseUnitTest

log=Logger(__name__,logging.DEBUG)
class TestLogin(BaseUnitTest):
    # 第一步执行的代码：setUpClass() 类前置
    # 第二步执行的代码：setUp()      方法前置
    # 第三步执行的代码是测试方法     ok
    # 第四步执行测试方法中的代码，直到完毕
    # 第五步执行的代码：tearDown()   方法后置
    # 第六步，找还有没有测试方法，有的话，执行方法前置setUp()
    # 第七步，第六步有的话，执行测试方法中的代码，直到完毕
    # 第八步，第六步有的话，执行tearDown()   方法后置
    # 第九步，找到还有没有的测试方法，无的话执行的代码是：tearDownClass()    类后置
    # 在测试中一个个测试方法就是测试用例

    # 测试用例+方法
    # 0登录成功-用户名、密码均正确
    def test_login_name_pwd_ok(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[0][0],self.loginPage.lginDataList[0][1])

        self.driver.implicitly_wait(10)
        sleep(3)
        # 获取登陆后的url
        self.url=self.driver.current_url
        # 判断是否是登录成功后的页面信息
        try:
            self.assertIn("dashboard",self.url)
        except Exception  as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("test_login_name_pwd_ok_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_pwd_ok_pass")
        #退出登录
        self.loginPage.logOutFun(self.driver)

    # 1登录失败-用户名空、密码空
    def test_login_name_pwd_no(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[1][0],self.loginPage.lginDataList[1][1])
        self.driver.implicitly_wait(5)
        # 判断是否登录失败
        # 判断手机号
        nameText=self.loginPage.getElementValue(self.loginPage.errorUname)
        try:
            self.assertEqual("请输入手机号码",nameText)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("test_login_name_pwd_no_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_pwd_no_pass")
            #判断密码
        pwdText=self.loginPage.getElementValue(self.loginPage.errorUpwd)
        try:
            self.assertEqual("请输入6-20位账户密码",pwdText)
        except Exception  as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("test_login_name_pwd_no_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_pwd_no_pass")
    # 2登陆失败，用户名空，密码正确
    def test_login_name_pwd_no_pwd_ok(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[2][0],self.loginPage.lginDataList[2][1])
        # 判断是否登录失败
        # 判断手机号
        nameText=self.loginPage.getElementValue(self.loginPage.errorUname)
        try:
            self.assertEqual("请输入手机号码",nameText)
        except Exception  as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("test_login_name_pwd_no_pwd_ok_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_pwd_no_pwd_ok_pass")
        # 判断密码
        # pwdText=self.loginPage.getElementValue(self.loginPage.errorUpwd)
        # self.assertEqual("请输入6-20位账户密码",pwdText)

    # 3登陆失败，用户名正确，密码空
    def test_login_name_pwd_no_name_ok(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[3][0],self.loginPage.lginDataList[3][1])

        # 判断是否登录失败
        # 判断手机号
        # nameText=self.loginPage.getElementValue(self.loginPage.errorUname)
        # self.assertEqual("请输入手机号码",nameText)
        # 判断密码
        pwdText=self.loginPage.getElementValue(self.loginPage.errorUpwd)
        try:
            self.assertEqual("请输入6-20位账户密码",pwdText)
        except Exception  as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("test_login_name_pwd_no_name_ok_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_pwd_no_name_ok_pass")
    # 4登录失败，用户名错误（用户名不存在），密码正确
    def test_login_name_false_pwd_true(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[4][0],self.loginPage.lginDataList[4][1])
        #获取弹窗错误信息
        errTxt=self.loginPage.getElementValue(self.loginPage.errMesage)
        # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误",errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("test_login_name_false_pwd_true_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_false_pwd_true_pass")
        #点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)

    # 5登录失败，用户名正确，密码错误
    def test_login_name_true_pwd_false(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[5][0],self.loginPage.lginDataList[5][1])
        #获取弹窗错误信息
        errTxt=self.loginPage.getElementValue(self.loginPage.errMesage)
        # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误",errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("test_login_name_true_pwd_false_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_true_pwd_false_pass")
        #点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)

    # 登陆失败，用户名错误，密码错误
    def test_login_name_false_pwd_false(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[6][0],self.loginPage.lginDataList[6][1])
        #获取弹窗错误信息
        errTxt=self.loginPage.getElementValue(self.loginPage.errMesage)
        # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误",errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("test_login_name_false_pwd_false_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_false_pwd_false_pass")
        #点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)

    # 用户名长度不够、密码正确
    def test_login_name_ell_pwd_true(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[7][0],self.loginPage.lginDataList[7][1])

        # 判断手机号
        nameText=self.loginPage.getElementValue(self.loginPage.errorUname)
        try:
            self.assertEqual("请输入手机号码",nameText)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("test_login_name_ell_pwd_true_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_ell_pwd_true_pass")
    # 登陆失败，用户名长度超出（12），密码正确
    def test_login_name_elm_pwd_true(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[8][0],self.loginPage.lginDataList[8][1])
        # 获取弹窗错误信息
        errTxt = self.loginPage.getElementValue(self.loginPage.errMesage)
        # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误", errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("test_login_name_elm_pwd_true_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_elm_pwd_true_pass")
        # 点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)
    # 用户名正确，密码长度不够
    def test_login_name_true_pwd_ell(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[9][0],self.loginPage.lginDataList[9][1])
        # 判断密码
        pwdText=self.loginPage.getElementValue(self.loginPage.errorUpwd)
        try:
            self.assertEqual("请输入6-20位账户密码",pwdText)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("test_login_name_true_pwd_ell_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_true_pwd_ell_pass")
    # 用户名正确，密码过长
    def test_login_name_true_pwd_elm(self):
        self.loginPage.loginFun\
            (self.loginPage.lginDataList[10][0],self.loginPage.lginDataList[10][1])
        # 获取弹窗错误信息
        errTxt = self.loginPage.getElementValue(self.loginPage.errMesage)
        # 断言弹窗错误信息
        try:
            self.assertIn("用户名或密码错误", errTxt)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("test_login_name_true_pwd_elm_faile")
        else:
            log.logger.info("断言成功！ ")
            self.loginPage.doPhoto("test_login_name_true_pwd_elm_pass")
        # 点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errBut)


if __name__ == '__main__':
    unittest.main()
