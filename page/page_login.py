import page
from Base.base import Base1



class PageLoginIndex(Base1):
    #关闭弹窗
    def page_click_alert(self):
        self.base_click(page.login_close_alert)

    def page_click_wo(self):
        self.base_click(page.login_me)
    def page_click_singin(self):
        self.base_click(page.login_close_alert)
    def page_send_number(self,phone):
        self.base_send_keys(page.login_phone.phone,phone)
    def page_send_pawd(self,pwd):
        self.base_send_keys(page.login_pwd,pwd)
    #点击登录按钮
    def page_click_login_buttn(self):
        self.base_click(page.login_btn)
    #点击签到按钮
    def page_click_sign_butt(self):
        self.base_click(page.login_sign)

    #点击处理异常

    #处理toast消息框
    def page_get_toast(self,msg):
        return self.base_get_toast(msg)

    def page_login_proxy(self,num,pwd):
        self.page_send_number(num)
        self.page_send_pawd(pwd)
        self.page_click_login_buttn()
        self.page_click_sign_butt()


