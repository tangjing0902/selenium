# -*- coding: UTF-8 -*-
from initialize.page.RegisterPage import RegisterPage
from webdriver.SeleniumDriver import SeleniumDriver

class Phone_edite(object):
    def __init__(self,driver):
        self.driver = driver
        self.logins = RegisterPage(self.driver)


    def __user_base(self,phone):
        self.logins.click_home_pop()
        self.logins.click_home_login()
        self.logins.send_phone(phone)


    def register_function(self,phone):
        self.__user_base(phone)
        return  self.logins.cheak_phone_value()

if __name__ == '__main__':
    driver = SeleniumDriver(SeleniumDriver.Chrome)
    driver.open_url_is_true("https://www.imooc.com/", "慕课网")
    driver.handle_windows(SeleniumDriver.Max)
    d = Phone_edite(driver).register_function("111111111111111111111111111111111111111111")
