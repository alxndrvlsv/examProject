import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Basket_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    """Basket 1"""
    price_product_1_cart = '//*[@id="tabs_cart"]/form/table/tbody[2]/tr/td[5]/div/b' # Цена первого товара
    price_product_2_cart = '//*[@id="tabs_cart"]/form/table/tbody[3]/tr/td[5]/div/b' # Цена второго товара
    summary_price_cart = '//*[@id="cartResultPrice__ID"]/div[1]' # Общая сумма покупки
    city_delivery_button = '//*[@id="basket_delivery__ID"]/div/span/a' #Выбор города доставки
    spb_city_delivery = '//*[@id="popup_cityselectnew"]/div/div[2]/div[1]/a[5]' #Город доставки Санкт-Петербург
    delivery = '//*[@id="js__productpage_deliveryPoint"]/tr[2]/td[1]/label/span[1]' #Доставка за пределы КАД
    сash_Payment = '//*[@id="basket_paymenttypes__ID"]/div/table/tbody/tr[3]/td[1]/label' #Оплата наличными
    arrange_order_button = '//*[@id="main_area"]/div[4]/div/form/div[2]/input' #Кнопка оформить заказ

    """Basket 2"""
    date_delivery = '//*[@id="delivery_date"]' # Дата доставки
    metro_Delivery = '//*[@id="station"]' # Метро доставки
    adress_Delivery = '//*[@id="address"]' # Адрес доставки
    name_Client = '//*[@id="contact__ID"]' # ФИО клиента
    mobile_Client = '//*[@id="cellphone__ID"]' # Телефон клиента
    order_Button = '//*[@id="order_step2_submit"]' # Кнопка Заказать

    # Getters

    """Basket 1"""

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

    def get_Cash_Payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.сash_Payment)))

    def get_arrange_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.arrange_order_button)))

    """Basket 2"""

    def get_date_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_delivery)))

    def get_Metro_Delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.metro_Delivery)))

    def get_Adress_Delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adress_Delivery)))

    def get_Name_Client(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_Client)))

    def get_Mobile_Client(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_Client)))

    def get_Order_Button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_Button)))

    # Action

    """Basket page 1"""

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
        self.get_Cash_Payment().click()
        print("Click Cash payment")

    def click_arrange_order_button(self):
        self.get_arrange_order_button().click()
        print("Click arrange order button")

    """Basket page 2"""

    def input_Adress_Delivery(self, adressDelivery):
        self.get_Adress_Delivery().send_keys(adressDelivery)
        print("Input Adress Delivery")

    def input_Name_Client(self, NameClient):
        self.get_Name_Client().send_keys(NameClient)
        print("Input Name Client")

    def input_Mobile_Client(self, MobileClient):
        self.get_Mobile_Client().send_keys(MobileClient)
        print("Input Mobile Client")

    def click_Order_Button(self):
        self.get_Order_Button().click()
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

    """"""
    def basket_step_1(self):
            self.authorization_basket()
            self.get_current_url()
            self.total_summary_price(self.get_price_product_1_cart(), self.get_price_product_2_cart(), self.get_summary_price_cart())
            self.click_city_delivery_button()
            self.click_spb_city_delivery()
            self.click_delivery()
            self.move_to_element(self.get_Cash_Payment())
            self.clickCashPayment()
            self.click_arrange_order_button()


    def basket_step_2(self):
            self.scroll_Down(self.get_date_delivery())
            self.scroll_Arrow_Down(self.get_Metro_Delivery(), 4)
            self.input_Adress_Delivery("Ленинградский проспект, дом. 81, кв. 77")
            self.input_Name_Client("Иван Иванов")
            self.input_Mobile_Client("+7(999)123-55-33")
            self.click_Order_Button()







