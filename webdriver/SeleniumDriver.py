# -*- coding: UTF-8 -*-

from webdriver import ElementUtlis
from selenium.webdriver.common.by import By
class SeleniumDriver(object):
    Chrome = "chrome"
    Firefox = "firefox"
    IE = "ie"
    Max = "max"
    Min = "min"
    Back = "back"
    Go = "go"
    F5 = "F5"
    Refresh="refresh"


    '''
    初始化打开浏览器
    '''

    def __init__(self, browser, configuration_file_download=True):
        self.driver = ElementUtlis.ElementUtlis(browser, configuration_file_download)


    '''
    打开网页，并判断打开的网页是否正确
    @parame url 网页地址
    @parame title_name 网页标题名称
    :return Flase True
    '''

    def open_url_is_true(self, url, title_name):
        return self.driver.open_url_is_true(url, title_name)

    '''
    获取页面info元素
    @parame info 元素定位的信息
    @return 查找成功返回一个元素 element   否则返回Flase
    '''

    def get_element(self, info):
        return self.driver.get_element(info)

    '''
    获取页面所有info元素
    @parame info 元素定位的信息
    @return elements 返回一个列表
    '''

    def get_elements(self, info):
        return self.driver.get_elements(info)

    '''
     通过父子层级获取页面info元素
     @parame info_level 父元素定位的信息
     @parame info_node 子元素定位的信息
     @return node_element 查找成功返回一个元素   否则返回Flase
     '''

    def get_leve_element(self, info_level, info_node):
        return self.driver.get_leve_element(info_level, info_node)

    '''
    网页的一些常用操作    
    参数为一个str 代表  max  min back  go 
    参数为多个 代表  设置网页大小
     '''

    def handle_windows(self, *args):
        self.driver.handle_windows(*args)

    '''
    根据传入的title，切换到相对应网页
    '''

    def switch_web_name(self,title_name):
        self.driver.switch_web_name(title_name)

    '''
    根据传入的index，切换到相对应网页
    '''
    def switch_web_index(self,index):
        self.driver.switch_web_index(index)

    def close_web_name(self,close_web_name,show_web_name):
        self.driver.close_web_name(close_web_name,show_web_name)

    '''
    切換iframe
    :param info iframe 元素信息
    '''
    def switch_iframe(self, info):
        self.driver.switch_iframe(info)

    '''
    处理系统弹框
    :param info iframe 元素信息

    '''

    def switch_alert(self, info, value=None):
        self.driver.switch_alert(info, value)

    '''
    获取页面info元素，并输入值
    @parame info 元素定位的信息
    :param value 输入值
    '''

    def send_value(self, info, value):
        self.driver.send_value(info, value)

    '''
    获取页面info元素，并点击
    :param info 元素定位的信息
    '''

    def click_element(self, info):
        self.driver.click_element(info)

    '''
    获取页面info元素
    开关 check 按钮 ，默认是关闭
    :param info 元素定位的信息
    '''
    def check_box_is_selected(self, info, check=False):
        self.driver.check_box_is_selected(info, check)


    def set_selected_Index(self, info, value_index, index=None):
        self.driver.set_selected_Index(info, value_index, index)


    def set_selected_Value(self,info,value,index):
        self.driver.set_selected_Value(info,value,index)



    def set_selected_visible_text(self,info,visible_text,index=None):
        self.driver.set_selected_visible_text(info,visible_text,index)

    '''
    文件上传
    :param file_name  文件路径
    :param info  非input类型上传文件/上传按钮元素信息
    :param send_info   input类型上传文件/input元素信息
    '''

    def upload_file_function(self, file_name, info=None, send_info=None):
        self.driver.upload_file_function(file_name, info, send_info)

    '''
    修改日历日期
    ;param info 元素定位的信息
    :param value 修改的值
    '''

    def set_calendar_value(self, info, value):
        self.driver.set_calendar_value(info, value)

    '''
    将鼠标移动到一个元素上面
    :param info 定位元素的信息
    '''

    def moveto_element_mouse(self, info):
        self.driver.moveto_element_mouse(info)

    '''
    滚动查找元素
    :param info 定位元素的信息
    '''

    def scroll_element(self, info):
        self.driver.scroll_element(info)

    '''
    等待查找元素
    :param info 定位元素的信息
    '''

    def wait_element(self, info):
        return self.driver.wait_element(info)

    '''
    等待查找元素
    :param info 定位元素的信息
    '''

    def wait_elements(self, info):
        return self.driver.wait_elements(info)

    '''
    截取整个网页图片,图片名称默认时间点
    :return 返回图片路径
    '''

    def save_screen(self, image_name=None):
        return self.driver.save_screen(image_name)

    '''
    截取元素区域图片,图片名称默认时间点  
    :param info 定位元素的信息
    :return 返回图片路径
    '''

    def get_element_screen(self, info, image_name=None):
        return self.driver.get_element_screen(info, image_name)

    '''
    获取页面info元素
    @parame info 元素定位的信息
    @return 返回element text文本信息
    '''

    def get_element_text(self, info):
        return self.driver.get_element_text(info)

    '''
    获取页面info元素
    @parame info 元素定位的信息
    @return 返回element vaule属性 text文本信息
    '''

    def get_element_value_text(self, info):
        return self.driver.get_element_value_text(info)
    '''
    获取页面info元素
    @parame info 元素定位的信息
    @parame tag 文本属性
    @return 返回element tag属性 text文本信息
    '''
    def get_element_tag_text(self, info, tag):
        return self.driver.get_element_tag_text(info, tag)

    def set_web_load_timeout(self,timeout=10):
        self.driver.set_web_load_timeout(timeout)

    def dump_html(self):
        self.driver.dump_html()
    '''
    关闭网页
    '''
    def close(self):
        self.driver.close()

if __name__ == '__main__':
    driver = SeleniumDriver(SeleniumDriver.Chrome)
    driver.open_url_is_true("https://www.imooc.com/","慕课网")
    driver.handle_windows(SeleniumDriver.Max)
    driver.click_element("click_login")
    driver.close()