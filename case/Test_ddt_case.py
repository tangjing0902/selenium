# -*- coding: UTF-8 -*-

from utlis.file.FileUtil import file_utils
from BeautifulReport.BeautifulReport import BeautifulReport
import unittest
from case import Test_ddt_case1,Test_ddt_case2,Test_ddt_case3





# 如果不能打开这个文件，可能是now的格式，不支持：和空格
# 报告地址&名称
report_title = "我的测试报告"

# 报告描述
desc = '汤金的报告'

if __name__ == '__main__':


    report_path = file_utils.location_file("report")
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.makeSuite(Test_ddt_case1.Test_ddt_case1))
    # testsuite.addTest(unittest.makeSuite(Test_ddt_case2.Test_ddt_case2))
    BeautifulReport.des=["第一个用例","第二个用例"]
    run = BeautifulReport(testsuite)
    run.report(description=desc, filename="我的报告", log_path=report_path)


