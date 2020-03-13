# -*- coding: UTF-8 -*-
from webdriver.SeleniumDriver import SeleniumDriver



if __name__ == '__main__':
    webdrive = SeleniumDriver(SeleniumDriver.Chrome)
    webdrive.open_url_is_true("https://www.baidu.com/",'百度一下')
    webdrive.wait_element()