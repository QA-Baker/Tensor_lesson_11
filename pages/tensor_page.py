from selenium.webdriver.common.by import By
from config import ABOUT_PAGE_URL
from pages.base_page import BasePage


class TensorPage(BasePage):
    NEWS_BLOCK = (By.XPATH, "//p[contains(@class, 'tensor_ru-Index__card-title') and text()='Сила в людях']")
    MORE_DETAILS_LINK = (By.CSS_SELECTOR, "a.tensor_ru-link.tensor_ru-Index__link[href='/about']")

    def is_news_block_present(self):
        """Проверить наличие блока 'Сила в людях'."""
        return bool(self.find_element(self.NEWS_BLOCK))

    def click_more_details(self):
        """Кликнуть по кнопке 'Подробнее'."""
        self.click_element(self.MORE_DETAILS_LINK)

    def is_about_page_opened(self):
        """Проверить, что открыта страница 'О компании'."""
        return self.get_current_url() == ABOUT_PAGE_URL
