# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5
"""
一、用例格式要求:
文件(module) :test_开头或 _test结尾
类: Test 开头
方法/函数: test开头
PS:测试用例类中不可以添加__init__构造函数(无法装载用例)
二、断言
表达式: 只有assert 预期结果==实际结果     ==可以换成!=/or/in/not in/is/not is
三、测试装置
1、setup_module/teardown_module  全局模块级(一个py文件)
2、setup_class/teardown_class    类级别，在类的前后只运行一次，setup_class类执行前运行，teardown——class类执行后运行一次
3、setup_method/teardown_method  方法级，类中的每个方法前后各执行一次
4、setup/teartown                在类中，运行在调用方法的前后各执行一次
"""
# import pytest
# def setup_module():
#     print("所有用例类的开始")
# def teardown_module():
#         print("所有用例类的ending")
# class TestClass:
#     @staticmethod
#     def setup_function():
#         print("这是setUpfunction")
#     @staticmethod
#     def teardown_function():
#         print("这是teardownfunction")
#     @staticmethod
#     def setup_class(cls):
#         print("zheshisetUpClass")
#     @staticmethod
#     def teardown_class(cls):
#         print("zheshiteardownclass")
#     def setup(self):
#         print("这是setUp")
#     def teardown(self):
#         print("这是teardown")
#     def test_one(self):
#         x='this'
#         assert "h" in x
#     def test_two(self):
#         x='hello'
#         assert "l" in x
# if __name__ == '__main__':
#     pytest.main()
#
import pytest
def setup_module():
    print("所有用例类的开始")
def teardown_module():
    print("所有用例类的结束")
class TestClass:
    @staticmethod
    def setup_function():
        print("这是setupfunction")
    @staticmethod
    def teardown_funcyion():
        print("这是teardownfunction")
    @staticmethod
    def setup_class(cls):
        print("zheshisetupclass")
    @staticmethod
    def teardown_class(cls):
        print("zheshiteardownclass")
    def setup(self):
        print("这是setUp")
    def teardown(self):
        print("这是teardown")
    def test_one(self):
        x="this"
        assert "h" in x
    def test_two(self):
        x="hello"
        assert "l" in x
if __name__ == '__main__':
    pytest.main()
