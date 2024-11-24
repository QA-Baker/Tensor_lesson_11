from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_url(self, url: str):
        """Открыть указанный URL."""
        self.driver.get(url)

    def find_element(self, locator):
        """Найти элемент с ожиданием."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Клик по элементу после того, как убедились что он доступен"""
        element = self.wait.until(EC.presence_of_element_located(locator))  # Убедиться, что элемент присутствует в DOM
        self.wait.until(EC.visibility_of(element))  # Убедиться, что элемент видим
        self.wait.until(EC.element_to_be_clickable(locator))  # Убедиться, что элемент кликабелен
        element.click()

    def switch_to_new_window(self):
        """Переключиться на новое окно."""
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    def get_current_url(self):
        """Получить текущий URL."""
        return self.driver.current_url
