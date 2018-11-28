from selenium.webdriver.common.by import By



# 立即体验按钮
experience_button = (By.ID,'com.kuaiduizuoye.scan:id/s_btn_go_new_version')
skip_button = (By.ID,'com.kuaiduizuoye.scan:id/sll_skip')
one_year_closebutton = (By.ID,'com.kuaiduizuoye.scan:id/iv_advertisement_widget_close')
my_button = (By.XPATH,'.//android.widget.TextView[@text="我的"]')
login_register_button = (By.ID,'com.kuaiduizuoye.scan:id/stv_login_or_register')
phone = (By.ID,'com.kuaiduizuoye.scan:id/et_phone')
nextstep_buton = (By.ID,'com.kuaiduizuoye.scan:id/s_btn_next')
password = (By.ID,'com.kuaiduizuoye.scan:id/et_password')
register_button = (By.ID,'com.kuaiduizuoye.scan:id/s_btn_login')
user_name = (By.ID,'com.kuaiduizuoye.scan:id/tv_user_name')
setting_button = (By.XPATH,'.//android.widget.TextView[@text="设置"]')
quit_register_button = (By.XPATH,'.//android.widget.TextView[@text="退出登录"]')
back_button = (By.ID,'com.kuaiduizuoye.scan:id/title_left_btn')
# 发送验证码
verification_code = (By.ID,'com.kuaiduizuoye.scan:id/tv_title')
# 未注册手机，发送验证码弹窗取消按钮
cancel_verification = (By.ID,'com.kuaiduizuoye.scan:id/btn_cancel')


del_button = (By.ID,'com.kuaiduizuoye.scan:id/siv_clear')
