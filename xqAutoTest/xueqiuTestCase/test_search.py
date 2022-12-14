import pytest,yaml
from page.app import APP
class TestSearch:
    @pytest.mark.parametrize("key,price",yaml.safe_load(open('D:\\PythonCoding\\xueqiuAutoTest\\Testdata\\search.yml')))
    def test_search001(self,key,price):
        assert APP().start().main().goto_search_page().searchinput(key).get_price()>float(price)
    def test_photo001(self):
        APP().start().main().goto_my_photo()