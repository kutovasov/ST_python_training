# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from group import Group


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def open_home_page(self, driver):
        driver.get("https://evernote.com/intl/ru/")

    def login(self, driver, username, password):
        driver.find_element_by_link_text(u"Войти").click()
        time.sleep(1)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("loginButton").click()
        time.sleep(1)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("loginButton").click()
        time.sleep(3)

    def create_note(self, driver, group):
        # init note creation
        driver.find_element_by_class_name("dropdown2").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/ul[1]/li[1]").click()
        time.sleep(1)
        # note creation
        driver.find_element_by_id("qa-NOTE_EDITOR_TITLE").clear()
        driver.find_element_by_id("qa-NOTE_EDITOR_TITLE").send_keys(group.name)
        driver.find_element_by_id("qa-NOTE_EDITOR_TITLE").send_keys(Keys.ENTER)
        time.sleep(1)

    def return_to_notes_page(self, driver):
        driver.find_element_by_id("qa-NAV_ALL_NOTES").click()

    def logout(self, driver):
        driver.find_element_by_id("qa-NAV_USER").click()
        driver.find_element_by_id("qa-ACCOUNT_DROPDOWN_LOGOUT").click()
        time.sleep(2)

    def test_add_note(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="kv-rnd@mail.ru", password="7Art9802")
        self.create_note(driver, Group(name="test"))
        self.return_to_notes_page(driver)
        self.logout(driver)

    def test_add_empty_note(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="kv-rnd@mail.ru", password="7Art9802")
        self.create_note(driver, Group(name=""))
        self.return_to_notes_page(driver)
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
