# -*- coding: UTF-8 -*-
import os
class FileUtil(object):





    '''
     定位到项目中文件路径 从项目根目录开始 
     '''
    def location_file(self,file_name):
        file_path =None
        path = os.path.split(os.path.realpath(__file__))[0]  # 定位类目录
        file_path = os.path.abspath(os.path.join(path, "..","..", file_name))  # 定位到项目根目录
        if os.path.exists(file_path):
            return file_path
        return file_path




file_utils = FileUtil()


