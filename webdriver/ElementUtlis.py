# -*- coding: UTF-8 -*-
import os

from selenium import webdriver
from utlis.read_res.handle_ini import handle_ini
from utlis.read_res.handle_json import handle_json
from utlis.Log.logger_config import logger
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver.WebDriverWait import WebDriverWait
from pykeyboard import PyKeyboard
from PIL import Image
from utlis.file.FileUtil import file_utils
import local_config
import time
class ElementUtlis(object):



    def __init__(self,browser,configuration_file_download):
        logger.info("========================================================测试开始========================================================")
        self.driver = self.__open_browser(browser,configuration_file_download)
        self.pkb = PyKeyboard()


    '''
   
    打开浏览器
    chrome:
        #download.default_directory：设置下载路径
        #profile.default_content_settings.popups：设置为 0 禁止弹出窗口
    firefox:
        browser.download.dir：指定下载路径
        browser.download.folderList：设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
        browser.download.manager.showWhenStarting：在开始下载时是否显示下载管理器
        browser.helperApps.neverAsk.saveToDisk：对所给出文件类型不再弹出框进行询问

    '''

    def __open_browser(self,browser,configuration_file_download):
        if browser == "chrome":
            options = webdriver.ChromeOptions()

            if configuration_file_download:
                prefs = {"profile.default_content_settings.popups": 0, "download.default_directory": local_config.FILE_DOWNLOAD_PATH}
                options.add_experimental_option("prefs",prefs)
            driver = webdriver.Chrome(executable_path=file_utils.location_file(local_config.CHROME_DRIVER_PATH),options=options)
        elif browser== "firefox":
            options = webdriver.FirefoxOptions()
            if configuration_file_download:
                options.set_preference("browser.download.dir",local_config.FILE_DOWNLOAD_PATH)
                options.set_preference("browser.download.folderList", "2")
                options.set_preference("browser.download.manager.showWhenStarting", False)
                options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
            driver = webdriver.Firefox(executable_path=file_utils.location_file(local_config.FIREFOX_DRIVER_PATH),options=options)
        elif browser== "ie":
            driver = webdriver.Ie(executable_path=file_utils.location_file(local_config.IE_DRIVER_PATH))
        else:
            driver = webdriver.edge()
        logger.info("当前测试浏览器:{0} ,下载文件路径配置:{1}".format(browser,local_config.FILE_DOWNLOAD_PATH))

        return driver



    '''
        获取页面info元素
        @parame info 元素定位的信息
        @return 查找成功返回一个元素 element  
    '''
    def get_element(self,info):
        by, value = self.get_local_element(info)
        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        else:
            return self.driver.find_element_by_xpath(value)
    '''
        显性等待查找元素
        @parame info 定位元素的信息
    '''
    def wait_element(self,info, timeout=12):
        return WebDriverWait(self.driver, timeout).until(self.get_element,info)





    """
        获取页面所有info元素
        @parame info 元素定位的信息
        @return elements 返回一个列表
    """
    def get_elements(self, info):
        by, value = self.get_local_element(info)
        if by == "id":
            elements = self.driver.find_elements_by_id(value)
        elif by == "name":
            elements = self.driver.find_elements_by_name(value)
        elif by == "class":
            elements = self.driver.find_elements_by_class_name(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        elif by == "text":
            return self.driver.find_elements_by_link_text(value)
        else:
            elements = self.driver.find_elements_by_xpath(value)
        return elements

    """
        显性等待获取页面所有info元素
        @parame info 元素定位的信息
        @return elements 返回一个列表
    """
    def wait_elements(self,info, timeout=12):
        return WebDriverWait(self.driver, timeout).until(self.get_elements, info)



    """
        通过当前节点定位子节点
        current_by:当前节点查找方式
        current_vlaue：当前节点元素信息
        info_by:子节点查找方式
        info_value:子节点元素信息
    """
    def get_leve_element(self, info_level, info_node):
        node_by, node_value = self.get_local_element(info_node)
        element = self.get_element(info_level)
        if element == False:
            return False
        if node_by == "id":
            node_element = element.find_element_by_id(node_value)
        elif node_by == "name":
            node_element = element.find_element_by_name(node_value)
        elif node_by == "class":
            node_element = element.find_element_by_class_name(node_value)
        elif node_by == "css":
            node_element = element.find_element_by_css_selector(node_value)
        elif node_by == "text":
            return self.driver.find_elements_by_link_text(node_value)
        else:
            node_element = element.find_element_by_xpath(node_value)
        return node_element




    """
        打开url网页     
    """
    def __get_url(self, url):
        if self.driver != None:
            if 'http' in url:
                logger.info("测试线上网页:{0}".format(url))
                self.driver.get(url)
            elif 'C' or 'D' or 'E' in url:
                self.driver.get(url)
            else:
                logger.info("测试本地网页:{0}".format(url))
        else:
            logger.info("你传入的url路径有误:{0}".format(url))



    """
        打开url网页,并判断当前网页title_name是否符合预期   
    """
    def open_url_is_true(self,url,title_name):
        self.__get_url(url)
        title_name_isture = self.assert_title(title_name)
        logger.info("当前网页:{0},结果:{1}".format(title_name, title_name_isture))
        return title_name_isture

    '''
        断言当前网页title是否正确
    '''
    def assert_title(self,title_name):
        logger.info(title_name)
        time.sleep(10)
        logger.info(str(self.driver.title))
        return title_name in str(self.driver.title)



    '''
        判断元素是否存在页面
    '''
    def element_isdisplayed(self,info):
        element = self.wait_element(info)
        return element.is_displayed()


    """
        输入文件路径,并按Ener
        file_path:文件路径
    """
    def __upload_file(self,file_path):
        self.pkb.type_string(file_path)
        time.sleep(2)
        self.pkb.tap_key(self.pkb.return_key)

    """
        通过js 移除日历readonly属性
    """
    def __js_execute_calendar(self,info):
        by,value=info
        if by == "id":
            by_key = "getElementById"
            js = 'document.%s("%s").removeAttribute("readonly");' %(by_key,value)
        else:
            by_key = "getElementClassName"
            js = 'document.%s("%s")[1].removeAttribute("readonly");' %(by_key,value)
        self.driver.execute_script(js)



    """
        浏览器操作
    """
    def handle_windows(self,*args):
        value = len(args)
        if value == 1:
            if args[0] == "max":
                self.driver.maximize_window()
            elif args[0] == "min":
                self.driver.minimize_window()
            elif args[0] == "back":
                self.driver.back()
            elif args[0] == "go":
                self.driver.forward()
            elif args[0] == "refresh":
                self.driver.refresh()
            elif args[0] == "F5":
                ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()
        elif value ==2:
            self.driver.set_window_size(args[0],args[1])
        else:
            logger.info("你传递的参数有问题")

    """
        根据传入的title_name，切换到相对应网页
    """
    def switch_web_name(self,title_name):
        hander_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in hander_list:
            if i!=current_handle:
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break

    """
        根据index，切换到相对应网页
    """
    def switch_web_index(self,index):
        hander_list = self.driver.window_handles
        if index>len(hander_list):
            logger.error("index < current_window_handle")
            raise Exception("index < current_window_handle ", index)
        self.driver.switch_to.window(hander_list[index-1])

    """
        根据index，切换到相对应网页
    """
    def close_web_name(self,close_web_name,show_web_name):
        hander_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in hander_list:
            if i!=current_handle:
                self.driver.switch_to.window(i)
                logger.info("3333333333")
                logger.info(self.assert_title(close_web_name))
                if self.assert_title(close_web_name):
                    logger.info("222222222222222222")
                    self.driver.close()
                    if close_web_name==show_web_name:
                        logger.info("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                        break
                    logger.info("1111111111")
                    close_web_name = show_web_name
                    close_web_name(close_web_name,show_web_name)


    """
        输入值
    """
    def send_value(self,info,key):
        self.wait_element(info).send_keys(key)
        logger.info("元素:{0}，输入值:{1}".format(info,key))



    """
        显性等待获取到元素，并点击元素
        info:元素信息
    """
    def click_element(self,info, timeout=20):
        self.wait_element(info,timeout).click()
        logger.info("点击元素:{0}".format(info))



    '''
        点击check元素
    '''
    def check_box_is_selected(self,info,check=False):
        element = self.wait_element(info)
        flag = element.is_selected()
        if check != flag:
            self.wait_element(info).click()


    '''
    通过index的值来设置 Select下拉框
    '''
    def set_selected_Index(self,info,value_index,index=None):
        selected_element= None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_index(value_index)


    '''
    通过value的值来设置 Select下拉框
    '''
    def set_selected_Value(self,info,value,index=None):
        selected_element= None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_value(value)

    '''
    通过visible_text的值来设置 Select下拉框
    '''
    def set_selected_visible_text(self,info,visible_text,index=None):
        selected_element= None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.wait_element(info)
        Select(selected_element).select_by_visible_text(visible_text)

    '''
        上传文件
        file_name:文件路径
        info:非input类型上传文件/上传按钮元素信息
        send_info:input类型上传文件/input元素信息
    '''
    def upload_file_function(self,file_name,info=None,send_info=None):
        if send_info:
            self.send_value(send_info,file_name)
        else:
            self.click_element(info)
            time.sleep(2)
            self.__upload_file(file_name)

    '''
    设置日历的值
    info:日历元素元素信息
    value:需要修改的值
    '''
    def set_calendar_value(self,info,value):
        element = self.wait_element(info)
        try:
            element.get_attribute("readonly")
            self.__js_execute_calendar(info)
        except:
            print("日历中没有readonly属性，可读可写")
        element.clear()
        self.send_value(info,value)


    '''
    将鼠标移动到一个元素上面
    info：定位元素的信息
    '''
    def moveto_element_mouse(self,info):
        element = self.wait_element(info)
        ActionChains(self.driver).move_to_element(element).perform()




    '''
    切换iframe
    '''
    def switch_iframe(self,info):
        if info!=None:
            iframe_element = self.wait_element(info)
            self.driver.switch_to_frame(iframe_element)
        else:
            self.driver.switch_to_default_content()
    '''
    点击系统弹框
    '''
    def switch_alert(self,info,value=None):
        if info=="accept":
            if value:
                self.driver.switch_to_alert().send_keys(value)
            self.driver.switch_to_alert().accept()
        else:
            self.driver.switch_to_alert().dismiss()

    '''
    滚动查找一个元素
    '''
    def scroll_element(self,info):
        js = 'document.documentElement.scrollTop=1000;'
        try:
            self.wait_element(info)
        except:
            self.driver.execute_script(js)
            pass




    '''
    得到当前网页的cookie数据
    '''
    def get_cookie(self):
        return self.driver.get_cookies()

    '''
      设置网页cookie
    '''
    def set_cookie(self):
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.driver.add_cookie(handle_json.get_data())




    def get_element_text(self,info):
        return self.wait_element(info).text

    def get_element_value_text(self,info):
        return self.wait_element(info).get_attribute("value")

    def get_element_tag_text(self,info,tag):
       if self.get_element(info) !=False :
            return self.wait_element(info).get_attribute(tag)






    '''
       截取element图片
    '''
    def get_element_screen(self,info,image_name=None):
        img_path = self.save_screen(image_name)
        location = self.wait_element(info).location
        size = self.wait_element(info).size
        left = location["x"]
        top = location["y"]
        right  = left+size["width"]
        bottom  = top+size["height"]
        img = Image.open(img_path)
        img = img.crop((left, top, right, bottom))
        img.save(img_path)
        return img_path



    '''
       整个页面截图
    '''
    def save_screen(self,img_name=None):
        if not img_name:
            img_name = time.strftime('%Y_%m_%d_%H_%M_%S')
        path = file_utils.location_file("config/image/"+img_name+".png")
        self.driver.save_screenshot(path)
        return path


    def set_web_load_timeout(self,timeout=10):
        self.driver.set_page_load_timeout(timeout)


    '''
       关闭浏览器
    '''
    def close(self):

        logger.info("========================================================测试结束========================================================")
        logger.info("\n")
        self.driver.close()
        self.driver.quit()


    def get_local_element(self, info):
        value = handle_ini.get_content("element", info)
        return self.parsing_content(value)



    def get_local_url(self, value):
        return handle_ini.get_content("url", value)



    def parsing_content(self, text_content):
        if text_content:
            return text_content.split("<")
        else:
            return False




    def get_web_driver(self):
        return self.driver

