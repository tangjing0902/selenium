#-*- coding: UTF-8 -*-
import time

from webdriver.SeleniumDriver import SeleniumDriver


url = "https://wetest.qq.com/"
atc_url = "https://atc.qq.com/"
task_name=""

if __name__ == '__main__':

    driver = SeleniumDriver(SeleniumDriver.Chrome)
    driver.handle_windows(SeleniumDriver.Max)
    driver.open_url_is_true(atc_url, "WeTest")
    driver.click_element("tapd_login")
    time.sleep(3)
    driver.switch_web_index(3)
    driver.send_value("username","t_jintang_ex")
    driver.send_value("password","123@abAB")
    driver.click_element("submit")


