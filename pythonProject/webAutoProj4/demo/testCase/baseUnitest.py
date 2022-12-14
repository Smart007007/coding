# coding="utf-8"
import unittest
from time import sleep

from selenium import webdriver

from demo.pageObject.loginPage import LoginPage


class BaseUnitTest(unittest.TestCase):
    # 类方法的前置
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化浏览器
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        print("setUpClass")

    # 方法级别的前置
    def setUp(self) -> None:
        # 定义登陆页面的实例化
        self.loginPage=LoginPage(self.driver)
        # 打开页面
        self.loginPage.open()
        print("我是setUp")

    # 方法级别的后置
    def tearDown(self) -> None:
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        print("我是teardown")

    # 类方法的后置
    @classmethod
    def tearDownClass(cls) -> None:
        # 退出浏览器
        cls.driver.quit()
        print("我是tearDownClass")