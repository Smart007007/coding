# coding="utf-8"
# log类，处理log文件
import logging

from common import config

class Logger(object):
    #实例化(初始化)方法
    def __init__(self, name, filelevel=logging.WARNING):
        # 定义一个记录器，日志对象，日志文件的实例
        self.logger=logging.Logger(name)

        # 定义日志输出等级
        self.logger.setLevel(filelevel)

        # 格式化模板
        fmt = logging.Formatter\
            ('%(asctime)s - '
             '%(filename)s:[%(lineno)s] - '
             '[%(levelname)s] - %(message)s')

        # 处理器，写信息到日志文件
        logname=config.log_path+config.cur_date+".log"
        #定义处理器
        fh=logging.FileHandler(logname,encoding="utf-8")
        # 指定让处理器按照什么格式来书写日志
        fh.setFormatter(fmt)

        # 将处理器加入记录器中：让处理器处理谁？-让处理器给谁干活~~~~~
        self.logger.addHandler(fh)

if __name__ == "__main__ " :
    # 实例化log日志对象
    logger=Logger(__name__,logging.DEBUG)
    # 写日志
    # CRITICAL = 50
    # FATAL = CRITICAL
    # ERROR = 40
    # WARING = 30
    # WARN = WARNING
    # INFO = 20
    # logging.DEBUG   =10
    # NOTSET = 0

    # 写debug级别的日志，等级
    # logger.logger.log(logging.DEBUG,'我是debug级别的日志，等级是10')
    logger.logger.debug('我是debug级别的日志，等级是10')
    # 写info级别的日志，等级20
    # logger.logger.log(logging.INFO,'我是info级别的日志，等级是20')
    logger.logger.info('我是info级别的日志，等级是20')
    # 写waring级别的日志，等级30
    # logger.logger.log(logging.WARNING,'我是warning级别的日志，等级是30')
    logger.logger.warning('我是warning级别的日志，等级是30')
    # #写error级别的日志，等级是40
    # logger.logger.log(logging.ERROR,'我是error级别的日志，等级是40')
    logger.logger.error('我是error级别的日志，等级是40')
    # #写critical级别的日志，等级是50
    # logger.logger.log(logging.CRITICAL,'我是critical级别的日志，等级是50')
    logger.logger.critical('我是critical级别的日志，等级是50')



