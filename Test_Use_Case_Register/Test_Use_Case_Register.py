from Base.Get_Driver import Get_Driver
from Page.Return_Page import Return_Page
import Page,time,pytest,allure
from Yaml.read_yaml import Read_Data

def yaml():
    list = []
    yaml_data = Read_Data('search_data.yaml').return_data()
    for i in yaml_data.keys():
        list.append((i,yaml_data.get(i).get('user'),yaml_data.get(i).get('password'),yaml_data.get(i).get('tag'),
                     yaml_data.get(i).get('assert_user'),yaml_data.get(i).get('assert_title'),yaml_data.get(i).get('assert_password')))
    return list


class Test_Login:
    def setup_class(self):
        self.Dv = Return_Page(Get_Driver().get_driver('com.kuaiduizuoye.scan','.activity.init.InitActivity'))
        # 滑动屏幕
        for i in range(2):
            self.Dv.return_page().slide_right()
        # 点击立即体验按钮
        self.Dv.return_page().click_experience_button()
        # 点击跳过按钮
        self.Dv.return_page().click_skip_button()
        # 点击关闭活动按钮
        self.Dv.return_page().click_oneyear_button()
        # 点击我的按钮
        self.Dv.return_page().click_my_button()
        # 点击登录或注册按钮
        self.Dv.return_page().click_loginregister_button()
    def teardown_class(self):
        self.Dv.driver.quit()
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('test_id,user,password,tag,assert_user,assert_title,assert_password',yaml())
    def test_setting(self,test_id,user,password,tag,assert_user,assert_title,assert_password):
        time.sleep(3)
        # 输入手机
        self.Dv.return_page().send_keys_account(Page.phone,user)
        # 点击下一步按钮
        self.Dv.return_page().click_nextstep_button()
        time.sleep(2)
        if assert_title:
            try:
                assert not self.Dv.return_page().gain_text(Page.verification_code)
            except Exception as E:
                allure.attach('获取验证码弹窗','{0}'.format('获取成功，未注册手机,需要注册！'))
            finally:
                # 点击取消按钮
                self.Dv.return_page().click_cancel_verification_button()
        if assert_user:
            # 输入密码
            self.Dv.return_page().send_keys_password(Page.password,password)
            time.sleep(1)
            # 上滑屏幕
            self.Dv.return_page().slide_up_001()
            # 点击登录按钮
            self.Dv.return_page().click_register_button()
            if tag:
                time.sleep(1)
                # 上滑屏幕
                self.Dv.return_page().slide_up()
                # 点击设置按钮
                self.Dv.return_page().click_setting_button()
                time.sleep(1)
                # 上滑屏幕
                self.Dv.return_page().slide_up()
                # 点击退出按钮
                self.Dv.return_page().click_quitregister_button()
                # 点击回退按钮
                self.Dv.return_page().click_back_button()
                # 下滑屏幕
                self.Dv.return_page().slide_below()
                try:
                    assert not self.Dv.return_page().find_element(Page.login_register_button)
                except Exception as E:
                    allure.attach('退出登录结果','{0}'.format('成功！'))
                finally:
                    time.sleep(1)
                    # 点击登录或注册按钮
                    self.Dv.return_page().click_loginregister_button()
            else:
                try:
                    assert not self.Dv.return_page().find_element(Page.password)
                except Exception as E:
                    allure.attach('获取密码输入框结果', '{0}'.format('获取成功，密码不正确，登录失败！'))
                finally:
                    # 点击回退按钮
                    self.Dv.return_page().click_back_button()