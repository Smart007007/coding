# 二、实现加、减、乘、除运算
# 1、运算区间0-200，其中任意一个数超出该区间，输出"运算数不在0-200区间范围内"
# 2、加法运算区间为100-200，任意一个数不在100-200区间内，输出"加法运算区间为100-200"，在该区间范围内才能进行加法运算
# 3、减法运算区间为40-99，任意一个数不在40-99区间内，输出"减法运算区间为40-99"，在该区间范围内才能进行减法运算，如果减数大于被减数，输出结果一定不能出现负数
# 4、乘法运算区间为20-39，任意一个数不在20-39区间内，输出"乘法运算区间为20-39"，在该区间范围内才能进行乘法运算
# 5、除法运算区间为0-19，，任意一个数不在0-19区间内，输出"除法运算区间为0-19"，在该区间范围内才能进行除法运算，且分母不能为0，如果为0 输出"除数为0，不能进行出发运算"
#     5.1第一个数为为11，第二数为2，做取余运算
#     5.2第一个数为为18，第二数为3，做取整运算
# 输出形式：例 100 + 200 =300
# 要求：
# 1、必须使用函数
#加法函数
def addfuntion(x,y):
    if 200>=x>=100 and 200>=y>=100:
        print(f"{x} + {y} =",x+y)
    else:
        print("加法运算区间为100-200")
#减法函数
def sub(x,y):
    if 99 >= x >= 40 and 99 >= y >= 40:
        print(f"{x} - {y} =", abs(x - y))
    else:
        print("减法运算区间为40-99")
#乘法函数
def mul(x,y):
    if 39 >= x >= 20 and 39 >= y >= 20:
        print(f"{x} * {y} =", abs(x * y))
    else:
        print("乘法运算区间为20-39")
#除法函数
def div(x,y):
    if 19 >= x >= 0 and 19 >= y >= 0:
        if y==0:
            if x==11 and y==2:
                print(f"{x} % {y} =",x%y)
            elif x==18 and y==3:
                print(f"{x} // {y} =",x//y)
            else:
                print(f"{x} / {y} =",x/y)
        else:
            print("两数都为0，不能进行计算！")
    else:
        print("除法运算区间为0-19")
#运算函数
def calcFunction():
    first=eval(input("请输入第一个数："))
    operator=input("请输入运算符：")
    second=eval(input("请输入第二个数："))
    if 200>=first>=0 and 200>=second>=0:
        if operator=="+":
            addfuntion(first,second)
        elif operator=="-":
            sub(first,second)
        elif operator=="*":
            mul(first,second)
        elif operator=="/":
            div(first,second)
        else:
            print("运算符不合法！")
    else:
        print("运算数不在0-200区间范围内")
#主函数
if __name__ == '__main__':
    calcFunction()
