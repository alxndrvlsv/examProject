import datetime
import re

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method Get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method Assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word = " + result)

    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + ' .png'
        self.driver.save_screenshot('C:\\Users\\Арина\\PycharmProjects\\examProject\\screen\\' + name_screenshot)

    """Method Assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method Move to element"""
    def move_to_element(self, locators):
        action = ActionChains(self.driver)
        action.move_to_element(locators).perform()
        print("Move to element")

    """Method Click and hold"""
    def click_and_hold(self, locators, x, y):
        action = ActionChains(self.driver)
        action.click_and_hold(locators).move_by_offset(x, y).release().perform()

    """Method scrolldown"""
    def scroll_Down(self, button):
        button.click()
        button.send_keys(Keys.DOWN)
        button.send_keys(Keys.ENTER)
        print("Scroll down OK")

    """Method scroll Arrow down"""
    def scroll_Arrow_Down(self, button, n):
        button.click()
        button.send_keys(Keys.ARROW_DOWN, n)
        button.send_keys(Keys.ENTER)
        print("Scroll Arrow down OK")




