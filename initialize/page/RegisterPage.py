# -*- coding: UTF-8 -*-
# from webdriver.SeleniumDriver import SeleniumDriver
class RegisterPage(object):

    def __init__(self,driver):
        self.driver = driver
        # self.driver = SeleniumDriver(SeleniumDriver.Chrome)
    #点击首页登录按钮
    def click_home_pop(self):
        return self.driver.click_element("click_pop")
    #点击首页登录按钮
    def click_home_login(self):
        return self.driver.click_element("click_login")

    #输入手机号码/或者邮箱输入
    def send_phone(self,vaule):
        return self.driver.send_value("phone",vaule)

    #输入密码
    def send_password(self,value):
        return self.driver.send_value("password",value)

    #登录按钮
    def click_login_submit(self):
        return self.driver.click_element("login_submit")

    #错误的手机号码/或者邮箱输入框提示
    def get_error_phone_text(self):
        return self.driver.get_element_text("phone_error")

    #错误的密码提示
    def get_element_password(self):
        return self.driver.get_element_text("password_error")


    def cheak_phone_value(self):
        return self.driver.get_element_value_text("phone")





    def get_error_text(self,info):
    #错误的手机号码/或者邮箱输入框提示
        try:
            if info=="usr_phone_error":
                return self.get_error_phone_text()
            elif info=="usr_password_error":
                return self.get_element_password()
            else:
                print ("你输入的信息有误")
        except:
            return None
