from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time, re

class LoginFuncional(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("c:\chromedriver")
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost:9090/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_funcional(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("| Login").click()
        driver.find_element_by_id("submit-login").click()
        driver.find_element_by_name("user_name").clear()
        driver.find_element_by_name("user_name").send_keys("Zizao Caixa")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_xpath("//div[@id='header']/div[2]/div/div/div/span/div/button").click()
        driver.find_element_by_link_text("Alterar Avatar").click()
        driver.find_element_by_name("file").clear()
        driver.find_element_by_name("file").send_keys("C:\\Users\\lucas.shen\\Downloads\\p.jpg")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
