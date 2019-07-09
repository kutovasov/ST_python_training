# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_note(self):
        driver = self.driver
        # Open home page
        driver.get("https://evernote.com/intl/ru/#")
        # login
        driver.find_element_by_link_text(u"Вход").click()
        time.sleep(0)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("kv-rnd@mail.ru")
        driver.find_element_by_id("loginButton").click()
        time.sleep(1)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("7Art9802")
        driver.find_element_by_id("loginButton").click()
        time.sleep(3)
        # init note creation
        driver.find_element_by_class_name("dropdown2").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/ul[1]/li[1]").click()
        time.sleep(1)
        # note creation
        driver.find_element_by_id("qa-NOTE_EDITOR_TITLE").clear()
        driver.find_element_by_id("qa-NOTE_EDITOR_TITLE").send_keys("test")
        time.sleep(1)
        driver.find_element_by_id("qa-NOTE_EDITOR_TITLE").send_keys(Keys.ENTER)
        # return to all notes page
        driver.find_element_by_id("qa-NAV_ALL_NOTES").click()
        # logout
        driver.find_element_by_id("qa-NAV_USER").click()
        driver.find_element_by_id("qa-ACCOUNT_DROPDOWN_LOGOUT").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
