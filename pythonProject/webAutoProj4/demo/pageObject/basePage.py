# coding="utf-8"
# 基础页面类存放所有页面可能用到的公共方法以及属性
# 所有page类均继承该基础类
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import config
from common.doExcel import DoExcel
from common.doLog import Logger

#定义log对象
log=Logger(__name__,logging.DEBUG)

#元素定位数据
testData=DoExcel()
class BasePage(object):
    # 定位登陆成功后右上角退出登录按钮
    # 右上角的个人头像
    img=(By.CSS_SELECTOR,".teachHeadPic.ng-star-inserted")
    # 退出账号
    logout=(By.XPATH,"//div[text()='退出账号']")
    # 退出账户的弹窗的确定按钮
    logoutOk=(By.CSS_SELECTOR,".ant-modal-confirm-btns>button:nth-child(2)")

    # 重构初始方法
    def __init__(self,driver,url=config.base_url):
        self.driver=driver
        self.url=url

    # 打开页面
    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("异常发生，页面打开失败，失败内容是：%s \n失败的页面是： %s"%(e,self.url))
            log.logger.critical\
                ("异常发生，页面打开失败，失败内容是：%s \n失败的页面是： %s"%(e,self.url),exc_info=True)
        else:
            print("未发生异常，页面打开成功！ %s"%self.url)
            log.logger.info("未发生异常，页面打开成功！ %s"%self.url)
            # self.driver.maximize_window()
            self.driver.implicitly_wait(10)

    # 定位元素
    def findElement(self,*locater):
        try:
            ele=WebDriverWait(self.driver,5,0.1).\
                until(EC.visibility_of_element_located(locater))
        except Exception as e:
            print("元素定位失败，错误信息是 %s，该元素是： %s"%(e,str(locater)))
            log.logger.error("元素定位失败，错误信息是 %s，该元素是： %s"%(e,str(locater)))
        else:
            print("元素定位成功，%s"%str(locater))
            log.logger.debug("元素定位成功，%s"%str(locater))
            # 定位成功之后需要return一下
            return ele

    # 文本框输入
    def inputValue(self, inputBox, value):
        # 定位元素
        ele=self.findElement(*inputBox)
        # 输入内容
        try:
            ele.send_keys(value)
        except Exception as e:
            print("输入内容%s失败，原因是：%s"%(value,e))
            log.logger.error("输入内容%s失败，原因是：%s"%(value,e))
        else:
            print("输入内容成功!")
            log.logger.info("输入内容成功")

    # 获取文本(标签)值
    def getElementValue(self,element):
        # 定位这个元素
        ele=self.findElement(*element)
        # 获取这个元素的文本值
        try:
            eleText=ele.text
        except Exception as e:
            print("获取文本失败%s失败，\n错误信息是： %s"%(str(element),e))
            log.logger.error("获取文本失败%s失败，\n错误信息是： %s"%(str(element),e),exc_info=True)
        else:
            print("文本获取成功，值是： %s"%eleText)
            log.logger.info("文本获取成功，值是： %s"%eleText)
            return eleText

    # 截图
    def doPhoto(self,name):
        filename=config.photo_path+config.cur_time+name+".png"
        try:
            self.driver.get_screenshot_as_file(filename)
        except Exception as e:
            print("截图失败，原因是：%s"%e)
            log.logger.error("截图失败，原因是：%s"%e)
        else:
            print("截图成功！")
            log.logger.info("截图成功！")

    # 元素点击
    def doClick(self,element):
        ele=self.findElement(*element)
        try:
            # ele.click()
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception as e:
            print("元素%s点击失败，原因是：%s"%(str(element),e))
            log.logger.error("元素%s点击失败，原因是：%s"%(str(element),e),exc_info=True)
        else:
            print("元素%s点击成功！"%str(element))
            log.logger.info("元素%s点击成功！"%str(element))

    # 退出登录
    def logOutFun(self,driver):
        action=ActionChains(driver)
        # 悬浮到头像上
        action.move_to_element(self.findElement(*self.img))
        action.perform()
        # 点击退出登录按钮
        # self.findElement(*self.logout).click()
        self.doClick(self.logout)
        sleep(3)

        # 点击弹窗中的确定按钮
        self.doClick(self.logoutOk)
        sleep(3)

if __name__=="__main__":
    driver=webdriver.Chrome()
    url="http://www.baidu.com"
    bspage=BasePage(driver,url)

    # 调用open方法
    bspage.open()
    bspage.driver.implicitly_wait(10)

    # 获取文本值。百度。雷小锋
    seting=(By.ID,"s-usersetting-top")
    print(bspage.getElementValue(seting))

    # 调用输入内容方法
    locater=(By.ID,"kw")
    bspage.inputValue(locater,"python")

    # 点击。百度。雷小锋
    but=(By.ID,"su")
    bspage.doClick(but)
    # 截图。百度。雷小锋
    bspage.doPhoto("test")

    bspage.driver.quit()
    # 第二个作业：创建一个py文件，命名：loginPage，
    # 在该文件中定义用户名、密码、登录按钮、错误信息。定义登录方法

# where和having的区别：having
# 1、都是条件过滤
# 2、where后面跟的是数据库表中已有的字段
# 3、where是在分组之前进行过滤
# 4、having一定是配合group by 进行使用
# 5、having后面的条件跟的是 聚合函数（count、min、max、avg、sum）
# 6、having是在分组之后进行的过滤
    # 数据库作业：学生表查询平均成绩大于70分的男生的学生信息
    # 过滤条件：avg(cj),sex
    # select count(*) from xsb;
    # select
    # select * avg(cj) from xsb where sex="男" group by sno having avg(cj)>70

    # 今天的数据库作业：查询出班级中同名的学生信息

