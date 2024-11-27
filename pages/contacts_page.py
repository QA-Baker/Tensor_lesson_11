from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.tensor_page import TensorPage


class ContactsPage(BasePage):
    TENSOR_BANNER = (By.CSS_SELECTOR,
                     "a.sbisru-Contacts__logo-tensor.mb-12[title='tensor.ru'][href='https://tensor.ru/']")

    def click_tensor_banner(self):
        self.click_element(self.TENSOR_BANNER)
        self.switch_to_new_window()
        return TensorPage(self.driver)
