import datetime
import logging
from utlis.file.FileUtil import file_utils
class LogUtils(object):


    def __init__(self,file_name=None):
        if file_name:
            self.file_path = file_utils.location_file("config/log/" + file_name + ".log")
        else:
            self.file_path = file_utils.location_file("config/log/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log")
        self.logger = logging.getLogger(__name__)
        # 这为清空当前文件的logging 因为logging会包含所有的文件的logging
        logging.Logger.manager.loggerDict.pop(__name__)
        # 将当前文件的handlers 清空
        self.logger.handlers = []
        # 然后再次移除当前文件logging配置
        self.logger.removeHandler(self.logger.handlers)
        if not self.logger.handlers:
            self.file_handler = logging.FileHandler(self.file_path)
            # logger 配置等级
            self.logger.setLevel(logging.DEBUG)
            #设置时间格式
            formatter = logging.Formatter("%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s -->%(message)s")
            #设置控制台输出
            stream_handler = logging.StreamHandler()

            self.file_handler.setFormatter(formatter)
            self.logger.addHandler(self.file_handler)
            self.logger.addHandler(stream_handler)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handler.close()
logger = LogUtils().get_log()