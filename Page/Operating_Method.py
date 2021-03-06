from appium.webdriver.common.touch_action import TouchAction

import Page,allure
from Base.Base_Method import Base_Method

class Operating_Method(Base_Method):
    def __init__(self,driver):
        Base_Method.__init__(self,driver)
    @allure.step('点击立即体验按钮')
    def click_experience_button(self):
        self.click_element(Page.experience_button)
    @allure.step('点击跳过按钮')
    def click_skip_button(self):
        self.click_element(Page.skip_button)
    @allure.step('点击活动关闭按钮')
    def click_oneyear_button(self):
        self.click_element(Page.one_year_closebutton)
    @allure.step('点击我的按钮')
    def click_my_button(self):
        self.click_element(Page.my_button)
    @allure.step('点击登录或注册按钮')
    def click_loginregister_button(self):
        self.click_element(Page.login_register_button)
    @allure.step('点击下一步按钮，断言是否跳转至密码输入页面')
    def click_nextstep_button(self):
        self.click_element(Page.nextstep_buton)
        try:
            assert self.find_element(Page.password)
        except Exception as E:
            allure.attach('是否跳转', '{0}'.format('未能跳转成功'))
    @allure.step('点击登录按钮,断言登录是否成功，获取我的账号')
    def click_register_button(self):
        self.click_element(Page.register_button)
        try:
            assert self.find_element(Page.register_button)
        except Exception as E:
            user_name = self.gain_text(Page.user_name)
            allure.attach('登录成功,我的账号','{0}'.format(user_name))
    @allure.step('获取text值')
    def gain_text(self,element):
        element = self.find_element(element)
        return element.text
    @allure.step('点击设置按钮')
    def click_setting_button(self):
        self.click_element(Page.setting_button)
    @allure.step('点击退出登录按钮，断言退出当前账号是否成功')
    def click_quitregister_button(self):
        self.click_element(Page.quit_register_button)
        try:
            assert self.find_element(Page.quit_register_button)
        except:
            allure.attach('是否退出成功', '{0}'.format('成功！'))
    @allure.step('点击回退按钮')
    def click_back_button(self):
        self.click_element(Page.back_button)
    @allure.step('点击获取验证码弹窗的取消按钮')
    def click_cancel_verification_button(self):
        self.click_element(Page.cancel_verification)

    @allure.step('页面向右滑动')
    def slide_right(self):
        TouchAction(self.driver).press(x=952, y=1007).move_to(x=14, y=984).release().perform()

    @allure.step('页面向上滑动')
    def slide_up(self):
        TouchAction(self.driver).press(x=466, y=1698).move_to(x=489, y=118).release().perform()

    @allure.step('页面向下滑动')
    def slide_below(self):
        TouchAction(self.driver).press(x=489, y=118).move_to(x=466, y=1698).release().perform()

    @allure.step('输入密码页面，向上滑动')
    def slide_up_001(self):
        TouchAction(self.driver).press(x=466, y=961).move_to(x=489, y=118).release().perform()