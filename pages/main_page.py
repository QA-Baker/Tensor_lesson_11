from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import BASE_URL
from pages.base_page import BasePage
from pages.contacts_page import ContactsPage


class MainPage(BasePage):
    CONTACTS_ELEMENT = (By.CSS_SELECTOR, "a.sbisru-Footer__link[href='/contacts']")

    def open(self):
        self.open_url(BASE_URL)

    def go_to_contacts(self):
        self.click_element(self.CONTACTS_ELEMENT)
        self.wait.until(EC.url_contains("/contacts"))
        return ContactsPage(self.driver)
