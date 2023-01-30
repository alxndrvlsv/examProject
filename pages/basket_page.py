import re
import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base
from utilities.logger import Logger


class Basket_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    """Basket 1"""
    continue_without_registration_button = '//*[@id="main_area"]/div[4]/div/div/div[2]/div/div/a[2]' #Кнопка продолжить без регистрации
    price_product_1_cart = '//*[@id="tabs_cart"]/form/table/tbody[2]/tr/td[5]/div/b' # Цена первого товара
    price_product_2_cart = '//*[@id="tabs_cart"]/form/table/tbody[3]/tr/td[5]/div/b' # Цена второго товара
    summary_price_cart = '//*[@id="cartResultPrice__ID"]/div[1]' # Общая сумма покупки
    city_delivery_button = '//*[@id="basket_delivery__ID"]/div/span/a' #Выбор города доставки
    spb_city_delivery = '//*[@id="popup_cityselectnew"]/div/div[2]/div[1]/a[5]' #Город доставки Санкт-Петербург
    delivery = '//*[@id="js__productpage_deliveryPoint"]/tr[2]/td[1]/label/span[1]' #Доставка за пределы КАД
    CashPayment = '//*[@id="basket_paymenttypes__ID"]/div/table/tbody/tr[3]/td[1]/label' #Оплата наличными
    arrange_order_button = '//*[@id="main_area"]/div[4]/div/form/div[2]/input' #Кнопка оформить заказ

    """Basket 2"""
    date_delivery = '//*[@id="delivery_date"]' # Дата доставки
    wordCashPayment = '//*[@id="main_area"]/div[4]/div/p/b[1]'
    wordDelivery = '//*[@id="main_area"]/div[4]/div/p/b[2]'
    metroDelivery = '//*[@id="station"]' # Метро доставки
    adressDelivery = '//*[@id="address"]' # Адрес доставки
    nameClient = '//*[@id="contact__ID"]' # ФИО клиента
    mobileClient = '//*[@id="cellphone__ID"]' # Телефон клиента
    orderButton = '//*[@id="order_step2_submit"]' # Кнопка Заказать

    # Getters

    """Basket 1"""
    def get_continue_without_registration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_without_registration_button)))

    def get_price_product_1_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1_cart)))

    def get_price_product_2_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2_cart)))

    def get_summary_price_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.summary_price_cart)))

    def get_city_delivery_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_delivery_button)))

    def get_spb_city_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.spb_city_delivery)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def getCashPayment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.CashPayment)))

    def get_arrange_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arrange_order_button)))

    """Basket 2"""

    def get_date_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_delivery)))

    def getWordCashPayment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.wordCashPayment)))

    def getWordDelivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.wordDelivery)))

    def getMetroDelivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.metroDelivery)))

    def getAdressDelivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adressDelivery)))

    def getNameClient(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nameClient)))

    def getMobileClient(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobileClient)))

    def getOrderButton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.orderButton)))

    # Action

    """Basket page 1"""
    def click_continue_without_registration_button(self):
        self.get_continue_without_registration_button().click()
        print("Сlick continue without registration button")

    def click_city_delivery_button(self):
        self.get_city_delivery_button().click()
        print("Click select city delivery")

    def click_spb_city_delivery(self):
        self.get_spb_city_delivery().click()
        print("Click city delivery")

    def click_delivery(self):
        self.get_delivery().click()
        print("Click delivery")

    def clickCashPayment(self):
        self.getCashPayment().click()
        print("Click Cash payment")

    def click_arrange_order_button(self):
        self.get_arrange_order_button().click()
        print("Click arrange order button")

    """Basket page 2"""

    def inputAdressDelivery(self, adressDelivery):
        self.getAdressDelivery().send_keys(adressDelivery)
        print("Input Adress Delivery")

    def inputNameClient(self, NameClient):
        self.getNameClient().send_keys(NameClient)
        print("Input Name Client")

    def inputMobileClient(self, MobileClient):
        self.getMobileClient().send_keys(MobileClient)
        print("Input Mobile Client")

    def clickOrderButton(self):
        self.getOrderButton().click()
        print("Click Order Button")

    def total_summary_price(self, price1, price2, summary_price):
        value_price_1 = price1.text
        vp_1 = [vp_1 for vp_1 in re.findall(r'\d+', value_price_1)]
        result_1 = int(str(vp_1[0]) + str(vp_1[1]))
        print(value_price_1)
        value_price_2 = price2.text
        vp_2 = [vp_2 for vp_2 in re.findall(r'\d+', value_price_2)]
        result_2 = int(str(vp_2[0]) + str(vp_2[1]))
        print(value_price_2)
        value_summary_price = summary_price.text
        print(value_summary_price)
        vsp = [vsp for vsp in re.findall(r'\d+', value_summary_price)]
        result_3 = vsp[0] + vsp[1]
        sum_result = str(result_1 + result_2)
        assert result_3 == sum_result
        print("Total Summary Price Good")

    # Methods

    def authorization_basket(self):
        with allure.step("Authorization basket"):
            Logger.add_start_step(method="authorization_cart")
            self.get_current_url()
            self.click_continue_without_registration_button()
            Logger.add_end_step(url=self.driver.current_url, method="authorization_cart")

    def basket_step_1(self):
        with allure.step("Basket Step 1"):
            Logger.add_start_step(method="basket_1")
            self.authorization_basket()
            self.get_current_url()
            self.total_summary_price(self.get_price_product_1_cart(), self.get_price_product_2_cart(), self.get_summary_price_cart())
            self.click_city_delivery_button()
            self.click_spb_city_delivery()
            self.click_delivery()
            self.move_to_element(self.getCashPayment())
            self.clickCashPayment()
            self.click_arrange_order_button()
            Logger.add_end_step(url=self.driver.current_url, method="basket_1")


    def basket_step_2(self):
        with allure.step("Basket Step 2"):
            Logger.add_start_step(method="basket_2")
            self.scroll_Down(self.get_date_delivery())
            self.scroll_Arrow_Down(self.getMetroDelivery(), 4)
            self.inputAdressDelivery("Ленинградский проспект, дом. 81, кв. 77")
            self.inputNameClient("Иван Иванов")
            self.inputMobileClient("+7(999)123-55-33")
            self.clickOrderButton()
            Logger.add_end_step(url=self.driver.current_url, method="basket_2")







