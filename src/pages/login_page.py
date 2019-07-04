# coding:utf-8
__author__ = 'Helen'
'''
description:登录页
'''
from appium.webdriver.common import mobileby
from src.common import base_page


class login_page(base_page.Base_page):
    by = mobileby.MobileBy()
    etUser_loc = (by.ID, "com.xsteach.appedu:id/etUser")
    etPws_loc = (by.ID, "com.xsteach.appedu:id/etPwd")
    btnLogin_loc = (by.ID, "com.xsteach.appedu:id/btnLogin")

    def input_user(self, username):
        self.send_keys(username, *self.etUser_loc)

    def input_Pws(self, password):
        self.send_keys(password, *self.etPws_loc)

    def click_btnLogin(self):
        self.find_element(*self.btnLogin_loc).click()
