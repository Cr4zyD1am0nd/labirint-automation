from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class LoginPage:
    """PageObject для страницы авторизации"""

    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[data-event-label='header-login']")
    EMAIL_INPUT = (By.ID, "login-email")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Открыть страницу авторизации")
    def open_login(self) -> None:
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    @allure.step("Ввести email: {1}")
    def enter_email(self, email: str) -> None:
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    @allure.step("Подтвердить ввод email")
    def submit(self) -> None:
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
