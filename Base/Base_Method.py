from selenium.webdriver.support.wait import WebDriverWait
import allure

class Base_Method:
    # 初始化driver
    def __init__(self,driver):
        self.driver = driver
    # 定位单个元素
    def find_element(self,loc,timeout=18,poll=0.1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    # 定位一组元素
    def find_elements(self,loc,timeout=18,poll=0.1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    # 点击
    def click_element(self,loc):
        self.find_element(loc).click()
    # 输入
    @allure.step('输入操作')
    def send_keys_account(self,loc,text):
        element = self.find_element(loc)
        element.clear()
        allure.attach('输入账号','{0}'.format(text))
        element.send_keys(text)
    @allure.step('输入操作')
    def send_keys_password(self, loc, text):
        element = self.find_element(loc)
        element.clear()
        allure.attach('输入密码', '{0}'.format(text))
        element.send_keys(text)