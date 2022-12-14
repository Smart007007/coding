# def regPage():
#     userinfo={"zhangsan":"123456",
#     "wanglaowu":"123456",
#     "chenxiaoliu":"123456",
#     "zhaolaoqi":"123456"}

#     if u in userinfo.keys():
#         if p==userinfo[u]:
#             return "登录成功！"
#         else:
#             return "用户名或密码错误！"
#
# def checkUserAndPwd():
#     if u in ["zhangsan","wanglaowu","chenxiaoliu","zhaolaoqi"]:
#         pass
#     else:
#         return "用户名密码错误！"
# def Loginpage():
#     userName=input("请输入用户名:")
#     password=input("请输入密码:")
#     checkUserAndPwd(userName,password)
#
# def mianPage():
#     pageMun=(input("请输入数字:"))
#     if pageMun==1:
#         pass

# """
# 登录、注册Function
# 1、输入1进入登录
# 2、输入2进入注册
# 3、输入非1/2，提示'请点击登录或者注册'
# 4、登录界面包含用户名和密码需校验用户名和密码匹配
# 5、注册界面包含用户名、密码、再次确认密码
#     5.1用户名长度为6-18位
#     5.2用户名不能重复
#     5.3密码长度为6-20，不能为纯数字
#     5.4确认密码与密码一致
# 二、实现加、减、乘、除运算
# 1、运算区间0-200，其中任意一个数超出该区间，输出"运算数不在0-200区间范围内"
# 2、加法运算区间为100-200，任意一个数不在100-200区间内，输出"加法运算区间为100-200"，在该区间范围内才能进行加法运算
# 3、减法运算区间为40-99，任意一个数不在40-99区间内，输出"减法运算区间为40-99"，在该区间范围内才能进行减法运算，如果减数大于被减数，输出结果一定不能出现负数
# 4、乘法运算区间为20-39，任意一个数不在20-39区间内，输出"乘法运算区间为20-39"，在该区间范围内才能进行乘法运算
# 5、除法运算区间为0-19，，任意一个数不在0-19区间内，输出"除法运算区间为0-19"，在该区间范围内才能进行除法运算，且分母不能为0，如果为0 输出"除数为0，不能进行出发运算"
#     5.1第一个数为为11，第二数为2，做取余运算
#     5.2第一个数为为18，第二数为3，做取整运算
#     5.3
#     5.4确认密码与密码一致
# 输出形式：例 100 + 200 =300
# 要求:
# 1、必须使用函数
# """
class MyFunction():
    def __init__(self):
        global userInfo
        userInfo={"zhangsan":"1234567",
                  "wanglaowu":"1234566",
                  "chenxiaoliu":"1234565",
                  "zhaoxiaoqi":"123456a"}
        def checkLoginUser(userName,password):
            if userName in userInfo.keys():
                if password==userInfo[userName]:
                    return "登录成功！"
                else:
                    return "用户名或密码不一致！"
            else:
                return "用户名或密码不一致！"
        #定义登录函数
        def LoginPage():
            userName=input("请输入用户名：")
            password=input("请输入密码：")
            print(userInfo.keys())
            result=checkLoginUser(userName,password)
            print(result)

        #定义注册函数
        def regPage():
            userName = input("请输入用户名：")
            if 18>=len(userName)>=6:
                if userName not in userInfo.keys():
                    password=input("请输入密码：")
                    if 20>=len(password)>=6:
                        if password.isdigit():
                            return "密码不能位纯数字！"
                        else:
                            Confirm_Password=input("请再次输入密码")
                            if Confirm_Password==password:
                                return "注册成功"
                            else:
                                return "两次密码不一致，请重新输入！"
                    else:
                        return "请输入6-20位的密码！"
                else:
                    return "用户名已存在，不能使用改用户名进行注册！"
            else:
                return "用户名不符合规则，6-18位！"
#我的页面
def myPage():
    my_btn=int(input("请输入一个数："))
    if my_btn==1:
        #调登录函数
        LoginPage()
    elif my_btn==2:
        #调注册函数
        reg_stu=regPage()
        print(reg_stu)
    else:
        print("请点击登录或注册")
#主程序入口
if __name__ == '__main__':
    myPage()








































































































































