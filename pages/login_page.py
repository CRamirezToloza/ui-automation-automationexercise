from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "[data-qa='login-email']")
    PASSWORD = (By.CSS_SELECTOR, "[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-qa='login-button']")
    TITLE = (By.XPATH, "//*[contains(text(),'Logged in as')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(),'Your email or password is incorrect')]")

    def login(self,email,password):
        self.type(self.USERNAME, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_loaded(self):
        logged_in_text = self.get_text(self.TITLE)
        return "Logged in as" in logged_in_text

    def login_error_message(self):
        login_error = self.get_text(self.ERROR_MESSAGE)
        return "Your email or password is incorrect" in login_error

