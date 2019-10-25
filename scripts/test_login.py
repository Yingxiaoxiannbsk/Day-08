import pytest

from page.pagein import PageIn
from tools.get_driver import GetDriver
def data():
    return [('18610453007','qq123456'),()]

class TestLogin:
    def setup_class(self):
        self.login= PageIn().page_login_in()
        self.index= PageIn().page_login_index()
        self.login.page_click_alert()
        self.login.page_click_wo()
        self.login.page_click_singin()
    def teardowm_class(self):
        self.driver= GetDriver.quit_driver()
    def test_login(self,num,pwd):
        self.login.page_login_proxy(num,pwd)
