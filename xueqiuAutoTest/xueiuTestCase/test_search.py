import os

import pytest,yaml,allure
from page.app import APP
@allure.feature("搜索模块")
class TestSearch:
    @pytest.mark.parametrize("key,price",yaml.safe_load(open('D:\\PythonCoding\\xueqiuAutoTest\\Testdata\\search.yml')))
    @allure.story("搜索框搜索公司股价")
    def test_search001(self,key,price):
        # step步骤
        with allure.step("1、首页点击搜索框进入搜索页面，输入关键词进行搜索，并断言"):
            assert APP().star().main().goto_search_page().searchinput(key).get_price()>float(price)
    # 点击头像进入我的页面
    @allure.story("点击头像进入我的页面")
    def test_photo001(self):
        APP().star().main().goto_my_photo()
# if __name__ == '__main__':
    # 生成到某个目录下
    # dirpatah="D:\\PythonCoding\\xueqiuAutoTest\\Testreport\\report"
    #
    # pytest.main(['./xueiuTestCase/test_search.py','-sv' ,"--alluredir",dirpatah])
    # os.system(f"allure generate {dirpatah} -o {dirpatah} --clean")