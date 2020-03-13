# -*- coding: UTF-8 -*-
from utlis.file.FileUtil import file_utils
import configparser
class HandIni(object):

    file_name ="config/element.ini"


    def __init__(self):
        self.data = self.loading_ini()



    '''定位ini文件'''
    def loading_ini(self):
        file_path = file_utils.location_file(self.file_name)
        file = configparser.ConfigParser()
        file.read(file_path, encoding="utf-8")
        return file




    def get_content(self,key,value):
        if key and value:
            return self.data.get(key,value)
        else:
            print("你输入的参数有误")


handle_ini = HandIni()


