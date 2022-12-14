#定义各种信息
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 定义浏览器对象

ba_url="http://baidu.com"
xlf_url="http://139.199.0.102/dashboard"
xyx_url="file:///C:/Users/007/Desktop/alert.html"
email_163_url="https://mail.163.com/"
qqemail_url="https://mail.qq.com/"

# 定义当前时间变量，且格式化：2022_11_17  16_35_30
cur_time=time.strftime("%Y_%m_%d %H_%M_%S")

def getDriver(url):
    try:
        driver=webdriver.Chrome()
    except Exception as e:
        print("发生异常，浏览器实例化失败！\n错误信息： %s"%e)
    else:
        print("未发生异常，浏览器实例化成功！ ")

    try:
        #打开页面
        driver.get(url)
    except Exception as e:
        print("页面打开失败： %s\n错误信息是： %s"%(url,e))
    else:
        print("未发生异常，页面被成功打开： %s"%url)
        # sleep(3)
        driver.implicitly_wait(3)
        return driver

def printCurrinfo(driver):
    cur_title = driver.title
    cur_url = driver.current_url
    cur_handle = driver.current_window_handle

    print("新页面信息开始打印~~~~~~~")
    print('当前页面的标题是：%s,\n当前页面url是： %s,\n当前页面句柄是 ：%s' % (
        cur_title, cur_url, cur_handle))
    print("新页面信息结束打印~~~~~~~")

# qq邮箱登录
def qqMailLogin(driver,vname,vpwd):
    # 定位iframe元素
    # ifram = driver.find_element_by_css_selector("[id^='login_frame']")
    ifram = findElement(driver,By.CSS_SELECTOR,"[id^='login_frame']")
    # 转移至frame
    driver.switch_to.frame(ifram)
    # 账号、密码、登录操作
    uname = driver.find_element_by_xpath("//form[@id='loginform']/div[1]/div[1]/input")
    password = driver.find_element_by_xpath("//form[@id='loginform']/div[2]/div[1]/input")
    dl = driver.find_element_by_xpath("//form[@id='loginform']/div[4]/a/input")
    # 登录失败，获取登录错误信息
    uname.clear()
    uname.send_keys(vname)
    password.clear()
    password.send_keys(vpwd)

    dl.click()
    # sleep(5)
    driver.implicitly_wait(2)
    errtext = driver.find_element(By.CSS_SELECTOR, "#err_m").text
    print("登录失败，信息是： %s" % errtext)
    # 回到主页面，定位右上角，手机版超链接
    driver.switch_to.default_content()

def findElement(driver,locater,value):
    #异常处理容易出错的代码块
    try:
        # ele=driver.find_element(locater,value)
        ele=WebDriverWait(driver,5,0.1).until(EC.visibility_of_element_located((locater,value)))
    #发生异常时,捕获异常，并让程序继续执行下一个操作
    #异常类型是Exception，且定义别名为e，并打印出异常信息
    except Exception as e:
        print("元素定位失败！！！ %s,\n错误信息是: %s"%(str(value),e))
    #未发生异常时，执行的代码块
    else:
        print("元素定位成功！！！ %s"%value)
        return ele
    # 不管是否发生异常，均执行的代码块
    finally:
        print("不管你成功还是失败你都要执行我！！！")

# 对点击做异常处理
def doClick(ele):
    try:
        ele.click()
    except Exception as e:
        print("发生异常，点击失败，错误信息是 %s"%e)
    else:
        print("未发生异常，点击成功")

# 对输入文本进行异常处理
def doInputvalue(ele,value):
    try:
        ele.send_key(value)
    except Exception as e:
        print("异常发生，输入内容失败内容是: %s\n错误信息是: %s"%(value,e))
    else:
        print("异常未发生，输入内容成功！！！ %s"%value)

# 截图
def dophoto(driver,value):
    filename=photos_path+cur_time+value+".png"
    try:
        driver.get_screenshot_as_file(filename)
        # driver.get_screenshot_as_file("aa.png")
    except Exception as e:
        print("截图失败，错误信息是: %s"%e)
    else:
        print("截图成功！！！")
# 定义一下项目路径
base_path=r"D:\PythonCoding\webAutoProject\\"
# 定义图片的存放路径：当前项目目录下的data目录下的photos目录下
photos_path=base_path+"/data/photos/"










