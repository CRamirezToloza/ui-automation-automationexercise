from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class ProductsPage(BasePage):
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    ADD_TO_CART_OVERLAY = (By.CSS_SELECTOR, ".overlay-content .add-to-cart")
    ADD_TO_CART_BUTTON_INSIDE = (By.CSS_SELECTOR, ".btn.btn-default.add-to-cart")
    ADDED_MODAL_TITLE = (By.XPATH, "//h4[contains(text(),'Added!')]")
    TITLE_VIEW_CART = (By.CSS_SELECTOR, "a[href='/view_cart']")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")
    MODAL_VIEW_CART_BUTTON = (By.CSS_SELECTOR, "#cartModal a[href='/view_cart']")

    def add_first_product_to_cart(self):
        # Obtener la lista de productos
        cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        # Primer producto visible
        first_card = cards[0]
        # Hover sobre el card
        ActionChains(self.driver).move_to_element(first_card).perform()
        # Buscar el botón Add to Cart dentro del card
        add_btn = first_card.find_element(*self.ADD_TO_CART_BUTTON_INSIDE)
        # Scroll
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
        # Hover + click
        ActionChains(self.driver).move_to_element(add_btn).click().perform()


    def add_products_to_cart(self, product_indexes):
       for index in product_indexes:
           cards = self.driver.find_elements(*self.PRODUCT_CARDS)
           product = cards[index]
           ActionChains(self.driver).move_to_element(product).perform()
           add_btn = product.find_element(*self.ADD_TO_CART_BUTTON_INSIDE)
           self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
           ActionChains(self.driver).move_to_element(add_btn).click().perform()

           if index != product_indexes[-1]:
               self.click(self.CONTINUE_SHOPPING)


    def is_product_added_modal_visible(self):
        text = self.get_text(self.ADDED_MODAL_TITLE)
        return "Added" in text

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def go_to_cart_from_popup(self):
        self.click(self.MODAL_VIEW_CART_BUTTON)














