# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://ru.wordpress.com/")
        driver.find_element_by_link_text(u"Войти").click()
        driver.find_element_by_id("usernameOrEmail").clear()
        driver.find_element_by_id("usernameOrEmail").send_keys("kv-rnd@mail.ru")
        driver.find_element_by_id("usernameOrEmail").send_keys(Keys.ENTER)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("7Art9802")
        driver.find_element_by_id("password").send_keys(Keys.ENTER)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Читалка'])[1]/following::span[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_id("post-title-0").clear()
        driver.find_element_by_id("post-title-0").send_keys("Test1")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Добавить запись'])[1]/following::button[6]").click()
        driver.find_element_by_css_selector("path").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Статус'])[1]/following::span[3]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Написать'])[1]/following::img[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@kutovasov'])[1]/following::button[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
