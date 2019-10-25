
import page
from Base.base import Base1


class PageIndex(Base1):
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)
    def page_click_setting(self):
        return self.base_click(page.login_logout)
    def page_click_logout_ok(self):
        return self.base_click(page.login_logout_ok)
    def page_logout(self):
        self.page_click_setting()
        self.page_logout()
        self.page_click_logout_ok()
