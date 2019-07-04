# coding:utf-8
__author__ = '???'
'''
description:测试登录和退出功能
'''
import unittest

from src.common import gesture_manipulation, driver_configure
from src.pages import login_page


class test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()
        cls.GM = gesture_manipulation.gesture_mainpulation()

    def test_01login(self):
        '''测试登录功能'''
        # 登录页
        self.login_page = login_page.login_page(self.driver)
        self.login_page.input_user("xybtest7@tf.com")
        self.login_page.input_Pws("qweqwe123")
        self.login_page.click_btnLogin()
        #self.assertEqual(u'签到', self.myInfo_page.getText_signHint())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
