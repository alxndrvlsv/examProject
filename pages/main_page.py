
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    catalog = '//a[@title="Каталог товаров"]'
    ofisnaya_tekhnika_category = '//a[@title="Перейти в категорию «Офисная техника»"]'
    calculator_category = '//a[@title="Перейти в категорию «Калькуляторы»"]'

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_ofisnaya_tekhnika_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ofisnaya_tekhnika_category)))

    def get_Calculator_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calculator_category)))

    # Action

    def click_catalog(self):
        self.get_catalog().click()
        print("Click Catalog")

    def click_Calculator_category(self):
        self.get_Calculator_category().click()
        print("Click Calculator category")

    # Methods

    """Выбор категории Калькуляторы"""
    def select_Calculator_category(self):
            self.get_current_url()
            self.click_catalog()
            self.move_to_element(self.get_ofisnaya_tekhnika_category())
            self.click_Calculator_category()




