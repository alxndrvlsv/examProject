import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


from base.base_class import Base
from utilities.logger import Logger


class Calculator_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    sort_Button = '//select[@id="js__listingSort_ID"]' # Сортировка товара
    mark_filter = '//label[@id="ld9b07a9490ffe0dd665e1991aa2a8c80"]'
    price_Filter = '//*[@id="search_form_id"]/div/div[5]/div[1]' # Цена
    left_Price_Filter = '//*[@id="js__ot_priceRange"]/span[1]' # Цена - левый ползунок
    right_Price_Filter = '//*[@id="js__ot_priceRange"]/span[2]'  # Цена - правый ползунок
    pick_Up_Filter_Button = '//*[@id="search_form_id"]/div/div[12]/a[1]' # Кнопка Подобрать
    product_Calc_1 = '//*[@id="item_container_1779773__ID"]/div[3]/div[3]/a' # Калькулятор настольный CITIZEN SDC-888TII
    product_Calc_2 = '//*[@id="item_container_845058__ID"]/div[3]/div[3]/a'# Калькулятор Citizen CT-555N
    continue_Shopping_Button = '//*[@id="popup_buy"]/div/div[2]/div/a[2]' # Кнопка Продолжить покупки
    Basket_Calc = '//*[@id="main_area"]/div[2]/div/div/div[4]/div[4]/a' # Корзина

    # Getters
    def get_Sort_Button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_Button)))

    def get_mark_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mark_filter)))

    def get_Price_Filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_Filter)))

    def get_Left_Price_Filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.left_Price_Filter)))

    def get_Right_Price_Filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.right_Price_Filter)))

    def get_Pick_Up_Filter_Button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_Up_Filter_Button)))

    def get_Product_Calc_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_Calc_1)))

    def get_Product_Calc_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_Calc_2)))

    def get_Continue_Shopping_Button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_Shopping_Button)))

    def get_Basket_Calc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Basket_Calc)))

    # Action

    def click_mark_filter(self):
        self.get_mark_filter().click()
        print("Click right now filter")

    def click_Pick_Up_Filter_Button(self):
        self.get_Pick_Up_Filter_Button().click()
        print("Click Pick up filter button")

    def click_Product_Calc_1(self):
        self.get_Product_Calc_1().click()
        print("Click Product calc 1")

    def click_Product_Calc_2(self):
        self.get_Product_Calc_2().click()
        print("Click Product calc 2")

    def click_Continue_Shopping_Button(self):
        self.get_Continue_Shopping_Button().click()
        print("Continue shopping")

    def click_Basket_Calc(self):
        self.get_Basket_Calc().click()
        print("Click Cart")


    # Methods

    def select_Filters(self):
        with allure.step("Select Filters"):
            Logger.add_start_step(method="select_Filters")
            self.click_mark_filter()
            self.get_Price_Filter().click()
            self.click_and_hold(self.get_Left_Price_Filter(), 10, 0)
            self.click_and_hold(self.get_Right_Price_Filter(), -100, 0)
            self.click_Pick_Up_Filter_Button()
            Logger.add_end_step(url=self.driver.current_url, method="select_Filters")

    def select_Products_Calc_1(self):
        with allure.step("Select Products Calc 1"):
            Logger.add_start_step(method="select_Products_Calc_1")
            self.move_to_element(self.get_Product_Calc_1())
            self.click_Product_Calc_1()
            self.click_Continue_Shopping_Button()
            Logger.add_end_step(url=self.driver.current_url, method="select_Products_Calc_1")

    def select_Products_Calc_2(self):
        with allure.step("Select Products Calc 2"):
            Logger.add_start_step(method="select_Products_Calc_2")
            self.move_to_element(self.get_Product_Calc_2())
            self.click_Product_Calc_2()
            self.click_Continue_Shopping_Button()
            Logger.add_end_step(url=self.driver.current_url, method="select_Products_Calc_2")

    def buy_Products_Calc(self):
        with allure.step("Buy Products Calc"):
            Logger.add_start_step(method="buy_Products_Calc")
            self.get_current_url()
            self.select_Filters()
            self.scroll_Arrow_Down(self.get_Sort_Button(), 1)
            self.select_Products_Calc_1()
            self.select_Products_Calc_2()
            self.click_Basket_Calc()
            Logger.add_end_step(url=self.driver.current_url, method="buy_Products_Calc")





