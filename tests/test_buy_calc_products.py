import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.calculator_page import Calculator_page
from pages.basket_page import Basket_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page

@allure.description("Test buy calc products")
def test_buy_calc_products():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service('C:\\Users\\Арина\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test")

    mp = Main_page(driver)
    mp.select_Calculator_category()

    cp = Calculator_page(driver)
    cp.buy_Products_Calc()

    bp = Basket_page(driver)
    bp.basket_step_1()
    bp.basket_step_2()

    f = Finish_page(driver)
    f.finish()

    print("Finish Test")
    time.sleep(10)


