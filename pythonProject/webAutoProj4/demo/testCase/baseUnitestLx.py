# coding="utf-8"
import unittest

from selenium import webdriver

from demo.pageObject.loginPage import LoginPage


class BaseUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.loginPage=LoginPage(self.driver)
        self.loginPage.open()

    def tearDown(self) -> None:
        self.driver.refresh()