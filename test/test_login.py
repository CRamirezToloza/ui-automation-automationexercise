from utils import configuration
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_success(driver):
    home = HomePage(driver)
    login_page = LoginPage(driver)

    # Ir a la home
    home.open(configuration.URL_APP_WEB)
    # Ir a Signup/Login
    home.go_to_signup_login()
    # Login con usuario existente
    login_page.login(configuration.EXISTING_USER_EMAIL, configuration.EXISTING_USER_PASSWORD)
    # Verificar que aparece "Logged in as ..."
    assert login_page.is_loaded()

def test_login_invalid_credentials(driver):
    home = HomePage(driver)
    login_page = LoginPage(driver)
    home.open(configuration.URL_APP_WEB)
    home.go_to_signup_login()
    # Credenciales incorrectas
    login_page.login("correo_incorrecto@example.com", "secret_sauce")
    # Verificar que se muestra el mensaje de error
    assert login_page.login_error_message()



