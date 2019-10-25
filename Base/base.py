import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_driver import GetDriver


class Base1:
    # 初始化
    def __init__(self):
        self.driver=GetDriver.get_driver()

    # 查找元素
    def base_find(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x: x.find_element(*loc))


    # 点击方法
    def base_click(self,loc):
        self.base_find(loc).click()

    # 输入方法
    def base_send_keys(self,loc,values):
        ele=self.base_find(loc)
        ele.clear()
        ele.send_keys(values)

    # 获取文本
    def base_get_text(self,loc):
        self.base_find(loc).text()

    def base_get_toast(self,msg):
        loc=By.XPATH,"//*[contains(@text,'{}')]".format(msg)
        self.base_find(loc,timeout=2,poll=0.5).text()
    def base_get_img(self):
        self.driver.get_screenshot_as_file('./image/err.png')
    def base_write_image(self):
        with open('./image/err.png','rb') as f:
            allure.attach("失败原因",f.read(),allure.attach_type.PNG)






