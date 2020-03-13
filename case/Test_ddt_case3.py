# -*- coding: UTF-8 -*-

from webdriver.SeleniumDriver import SeleniumDriver
from initialize.busines.Phone_edite import Phone_edite
from utlis.read_res.handle_exec import read_exec
import unittest
import ddt

data = read_exec.get_data()

@ddt.ddt
class Test_ddt_case3(unittest.TestCase):


    def setUp(self):
        self.web_tools = SeleniumDriver(SeleniumDriver.Chrome)
        self.phone_edite = Phone_edite(self.web_tools)
        self.web_tools.open_url_is_true("https://www.imooc.com/","慕课网")
        self.web_tools.handle_windows(SeleniumDriver.Max)

    @ddt.data(*data)
    def test_register_case(self,data):
        phone,passwrod,error_cod,assert_text = data
        rest = self.phone_edite.register_function(phone)
        self.assertEqual(len(rest),37,"预期结果错误")

    def tearDown(self):
        self.web_tools.close()

