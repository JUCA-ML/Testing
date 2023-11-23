import time
import unittest
from selenium import webdriver
from tasks.login_page import LoginPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Test_Login(unittest.TestCase):

    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    __user = 'standard_user'
    __password = 'secret_sauce'

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test1_login(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)
        driver = self.driver
        LoginPage().enter_credential(driver, self.__user, self.__password)

    def test2_button(self):
        LoginPage().on_clickLogin(self.driver)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        pass
        #cls.driver.quit()
