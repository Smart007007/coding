import unittest

from common import doSuit, doReport

if __name__ == '__main__':
    # 获取测试套件
    suit=unittest.TestSuite()
    # 通过第一种方式获取，需要第一步的suit对象
    suit=doSuit.addTestByMethod(suit)
    # 通过第二种方式获取，需要第一步的suit对象
    suit=doSuit.addTestByClass(suit)
    # 通过第三种方式获取不需要第一步的suit对象们会自动生成与以一个
    # suit=doSuit.addTestByAuto()
    # 执行套件，并在控制台打印测试用例执行情况
    # run=unittest.TextTestRunner(verbosity=2)
    # # run.run(suit)

    # 执行并生成测试报告，text
    # doReport.doTextReport(suit)
    # 执行并生成测试报告，html
    # doReport.doHTMLReport(suit)
    # 执行并生成测试报告，html格式更美观
    doReport.doHTMLReportBeautiful(suit)



















    # list1=[29,12,89,30,90,49]
    # # 冒泡排序，从大到小
    # i=0
    # for i in range(0,len(list1)-1):
    #     for j in  range(i+1,len(list1)):
    #         if list[i]<list[j]:
    #             list1[i],list[j]=list1[j],[i]
    #         print("第%s,%s次小循环"%(i,j),list1)
    #     print("第%d次大循环"%(i+1),list1)
    # print("循环结束",list1)