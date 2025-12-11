from utils import configuration
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage


def test_add_first_product_to_cart(driver):
    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    home.open(configuration.URL_APP_WEB)
    products.add_first_product_to_cart()
    products.go_to_cart_from_popup()
    assert cart.get_number_of_products() > 0, "No se encontró ningún producto en el carrito"

def test_add_products_to_cart(driver):
    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    home.open(configuration.URL_APP_WEB)
    products_to_add = [1, 5, 7]
    products.add_products_to_cart(products_to_add)
    products.go_to_cart_from_popup()
    num_products = cart.get_number_of_products()
    assert  num_products == len(products_to_add)

    prices = cart.get_product_prices()  # [500, 400, ...]
    quantities = cart.get_product_quantities()  # [1, 2, ...]
    actual_totals = cart.get_product_totals()  # [500, 800, ...]

    assert len(prices) == len(quantities) == len(actual_totals) == num_products, (
        "La cantidad de precios, cantidades y totales no coincide con "
        "el número de productos en el carrito.")

    # Obtener los totales esperados calculados por CartPage
    expected_totals = cart.get_expected_totals()  # [price * qty para cada producto]

    # Comparar totales esperados vs totales mostrados
    assert actual_totals == expected_totals, (
        f"Los totales del carrito no son correctos.\n"
        f"Esperado: {expected_totals}\n"
        f"Actual:   {actual_totals}")











