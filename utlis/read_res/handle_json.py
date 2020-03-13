# -*- coding: UTF-8 -*-

from utlis.file.FileUtil import file_utils
import json
class HandleJson(object):
    file_name = "config/cookie.json"
    def __init__(self):
        self.path_name = self.loading_json()
        pass

    '''定位json文件'''
    def loading_json(self):
        return file_utils.location_file(self.file_name)


    '''读取json信息'''
    def get_data(self):
        with open(self.path_name) as info:
            data = json.load(info)
        return data


handle_json = HandleJson()
