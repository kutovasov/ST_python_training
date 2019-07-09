# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_record(self):
        driver = self.driver
        # Open home page
        driver.get("https://ru.wordpress.com/")
        # login
        driver.find_element_by_link_text(u"Войти").click()
        time.sleep(1)
        driver.find_element_by_id("usernameOrEmail").clear()
        driver.find_element_by_id("usernameOrEmail").send_keys("kv-rnd@mail.ru")
        driver.find_element_by_id("usernameOrEmail").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("7Art9802")
        driver.find_element_by_id("password").send_keys(Keys.ENTER)
        time.sleep(1)
        # init record creation
        driver.find_element_by_class_name("masterbar__publish").click()
        time.sleep(8)
        # fill form
        #driver.find_element_by_id("post-title-0").clear()
        #driver.find_element_by_id("post-title-0").send_keys(u"ТЕСТ")
        driver.find_element_by_class_name("editor-post-title__input").clear()
        driver.find_element_by_class_name("editor-post-title__input").send_keys("Test1")
        time.sleep(2)
        # record saving
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Добавить запись'])[1]/following::button[6]").click()
        time.sleep(2)
        # return to records page
        driver.find_element_by_css_selector("path").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Статус'])[1]/following::span[3]").click()
        # logout
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Написать'])[1]/following::img[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@kutovasov'])[1]/following::button[1]").click()


    def tearDown(self):
        #self.driver.close()
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
