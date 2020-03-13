# -*- coding: UTF-8 -*-
from initialize.page.RegisterPage import RegisterPage
class MkLogin(object):

    def __init__(self,driver):
        self.driver = driver
        self.logins = RegisterPage(self.driver)


    def __user_base(self,phone,password):
        self.logins.click_home_pop()
        self.logins.click_home_login()
        self.logins.send_phone(phone)
        self.logins.send_password(password)
        self.logins.click_login_submit()



    def register_function(self,phone,password,error_cod,assert_text):
        self.__user_base(phone,password)
        error_info = self.logins.get_error_text(error_cod)
        if error_info == assert_text:
            return True
        else:
            return False









