"""
四、pytest参数化
1 单参数: @pytest.mark.parametrize装饰器第一个参数要和用例单参数一致
        装饰器的第二个参数传的一个列表，每一个值代表一个数据
        装饰器的第三个参数，选传参数，传的是用例标题，列表表示，前面有几个数据，后面对应几个标题
2 多参数:第一个参数要和测试用例的参数一致
        第二个参数传入一个列表，每个值需要用个迭代的对象(元组)进行包裹，元组内的数据量要和参数的数据量相同，代表一个数据
五、用例标记---使用场景:只去执行一部分特定用例
使用方法:@pytest.mark.标签名
执行方法:pytest test_demo.py -m 标签名
"""
import pytest
# import pytest
# # #单参数
# search_list=["111","000",'ccc']
# @pytest.mark.parametrize("key_word",['111','000','ccc'],ids=['测试搜索111','测试搜索000','测试搜素ccc'])
# def test_search(key_word):
#     assert key_word in search_list

#多参数
# @pytest.mark.parametrize("input_value,expValue",[("1+1",2),("2*3",6),("10/2",5)])
# def test_calc(input_value,expValue):
#     assert eval(input_value)==expValue
#笛卡尔积
# @pytest.mark.parametrize('x',[1,2,3])
# @pytest.mark.parametrize('y',['第一组','第二组'])
# def test_foo(x,y):
#     print('{}第{}个数'.format(y,x))

@pytest.mark.login
def test_login_001():
    print("用户名密码登录成功")
@pytest.mark.login
def test_login_002():
    print("用户名密码登录失败")
@pytest.mark.login
def test_login_003():
    print("手机号一键登录")
@pytest.mark.reg
def test_reg_001():
    print('用户名已存在')
@pytest.mark.reg
def test_reg_002():
    print("注册成功")
@pytest.mark.reg
def test_reg_003():
    print("密码不合规")