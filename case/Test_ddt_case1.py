# -*- coding: UTF-8 -*-
from webdriver.SeleniumDriver import SeleniumDriver
from initialize.busines.MkLogin import MkLogin
from utlis.read_res.handle_exec import read_exec
import unittest
import ddt
data = read_exec.get_data()

@ddt.ddt
class Test_ddt_case1(unittest.TestCase):


    def setUp(self):
        self.web_tools = SeleniumDriver(SeleniumDriver.Chrome)
        self.mlgoin = MkLogin(self.web_tools)
        self.web_tools.open_url_is_true("https://www.imooc.com/","慕课网")
        self.web_tools.handle_windows(SeleniumDriver.Max)
    


    @ddt.data(*data)
    def test_register_case(self,data):
        phone,passwrod,error_cod,assert_text = data
        rest = self.mlgoin.register_function(phone, passwrod, error_cod, assert_text)
        self.assertTrue(rest,"预期结果错误")



    def tearDown(self):
        self.web_tools.close()



