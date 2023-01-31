import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    word_Order = '//*[@id="main_area"]/div[5]/div/h1'
    cansel_Order_Button = '//*[@id="main_area"]/div[5]/div/div[7]/a' # Кнопка Отмена заказа
    confirm_Cansel_Order_Button = '//*[@id="popup_message"]/div[2]/a[1]' # Кнопка подтверждения отмены заказа

    # Getters

    def get_Word_Order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_Order)))

    def get_Cansel_Order_Button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cansel_Order_Button)))

    def get_Confirm_Cansel_Order_Button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_Cansel_Order_Button)))

    # Action

    def click_Cansel_Order_Button(self):
        self.get_Cansel_Order_Button().click()
        print("Click Cansel Order Button")

    def click_Confirm_Cansel_Order_Button(self):
        self.get_Confirm_Cansel_Order_Button().click()
        print("Click Confirm Cansel Order Button")

    # Methods
    def finish(self):
            self.get_current_url()
            self.assert_word(self.get_Word_Order(), "Заказ оформлен!")
            self.get_screenshot()
            self.click_Cansel_Order_Button()
            self.click_Confirm_Cansel_Order_Button()
