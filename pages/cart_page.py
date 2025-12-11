from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helpers import extract_digits_from_elements

class CartPage(BasePage):
    CART_ROWS = (By.CSS_SELECTOR, "tr[id^='product']")
    PRODUCT_PRICES = (By.CSS_SELECTOR, "tr[id^='product'] .cart_price")
    PRODUCT_QUANTITIES = (By.CSS_SELECTOR, "tr[id^='product'] .cart_quantity")
    PRODUCT_TOTALS = (By.CSS_SELECTOR, "tr[id^='product'] .cart_total_price")

    def get_number_of_products(self):
        rows = self.driver.find_elements(*self.CART_ROWS)
        return len (rows)

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return extract_digits_from_elements(elements)

    def get_product_quantities(self):
        elements = self.driver.find_elements(*self.PRODUCT_QUANTITIES)
        return extract_digits_from_elements(elements)

    def get_product_totals(self):
        elements = self.driver.find_elements(*self.PRODUCT_TOTALS)
        return extract_digits_from_elements(elements)

    def get_expected_totals(self):
        prices = self.get_product_prices()
        quantities = self.get_product_quantities()
        return [price * qty for price, qty in zip(prices, quantities)]







