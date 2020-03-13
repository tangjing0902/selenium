# -*- coding: UTF-8 -*-
import time
from utlis.file.FileUtil import file_utils
from PIL import ImageGrab


class Save_Img(object):

    def __init__(self):
        self.img = ImageGrab.grab(all_screens=True)


    '''
       整个页面截图
    '''
    def save_screen(self,img_name=None):
        if not img_name:
            img_name = time.strftime('%Y_%m_%d_%H_%M_%S')
        print(img_name)
        path = file_utils.location_file("config/image/" + img_name + ".jpg")
        print(path)
        self.img.save(path)
        return path

