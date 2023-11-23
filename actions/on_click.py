from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OnClick:
    def on_click(self, driver: webdriver, locator):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, locator))).click()
