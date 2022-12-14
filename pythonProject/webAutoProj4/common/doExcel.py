# coding="utf-8"
#处理excel文件
import xlrd

from common import config
from common.doLog import Logger

log=Logger(__name__)
class DoExcel(object):
    #重构初始化方法
    def __init__(self,wk='testData.xlsx',st='elements'):
        filename=config.data_path+wk
        try:
            #打开工作簿
            self.workbook=xlrd.open_workbook(filename)
            # #获取sheet页,三种方式获取sheet页
            # stnames=self.workbook.sheet_names()
            #
            # print(stnames)
            # #第一种：列表的下标
            # self.sheet=self.workbook.sheet_names()[0]
            # #第二种：索引     index
            # self.sheet=self.workbook.sheet_by_index(0)
            # 第三种：sheet名称, 下标和索引可能会出现问题
            self.sheet=self.workbook.sheet_by_name(st)
        except Exception as e:
            log.logger.error\
                ("工作簿或者sheet页未实例化成功，原因是 %s"%e,exc_info=True)
        else:
            log.logger.info("工作簿或者sheet页面打开成功,值是： %s"%wk)

    #读取单元格的值
    def readExcel(self,rownum,colnum):
        try:
            value=self.sheet.cell_value(rownum,colnum)
        except Exception as e:
            # print("%s读取文件异常"%e)
            log.logger.error\
                ("该单元格值(%s,%s)获取失败,错误信息是：%s"%(rownum,colnum,e),exc_info=True)
        else:
            # print("读取文件成功。值是：%s"%value)
            log.logger.info\
                ("单元格值(%s,%s)文件获取成功,值是：%s"%(rownum,colnum,value))
            return value


#自测方法
if __name__=="__main__":
    ex=DoExcel()
    value=ex.readExcel(7,4)
    print(value)