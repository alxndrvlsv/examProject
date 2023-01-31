from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Registration_page(Base):

    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    enter_personal_account = '//span[@class="ic__set ic__set__member"]'  # Вход в личный кабинет
    registration_button = '//a[@class="formLines__registerLink"]'  # Кнопка Регистрация
    name = '//input[@id="contact"]'  # Ввод имени
    e_mail = '//input[@id="email"]'  # Ввод e-mail
    password = '//input[@id="account_myPasswordEdit_2ID"]'  # Ввод пароля
    mobile_number = '//input[@id="cellphone"]'  # Ввод мобильного номера
    register_button = '//input[@class="button button__orange js__formBoxMainButton"]'  # Кнопка зарегистрироваться

    # Getters

    def get_enter_personal_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_personal_account)))

    def get_registration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_button)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_e_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.e_mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_mobile_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_number)))

    def get_register_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.register_button)))


    # Action

    def click_enter_personal_account(self):
        self.get_enter_personal_account().click()
        print("Сlick enter personal account")

    def click_registration_button(self):
        self.get_registration_button().click()
        print("Click registration button")

    def input_name(self, name):
        self.get_name().send_keys(name)
        print("Input name")

    def input_e_mail(self, e_mail):
        self.get_e_mail().send_keys(e_mail)
        print("Input e-mail")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def input_mobile_number(self, mobile_number):
        self.get_mobile_number().send_keys(mobile_number)
        print("Input mobile number")

    def click_register_button(self):
        self.get_register_button().click()
        print("Click register button")

    # Methods

    """Регистрация аккаунта"""
    def register_account(self):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_enter_personal_account()
            self.click_registration_button()
            self.input_name("Ivan Ivanov")
            self.input_e_mail("register@aol.com")
            self.input_password("passowrd123")
            self.input_mobile_number("+79115551133")
            # self.click_register_button()
