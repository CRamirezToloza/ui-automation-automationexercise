import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    # Si quieres que no se abra la ventana, puedes agregar:
    # options.add_argument("--headless=new")

    # 👉 Aquí usamos webdriver-manager para descargar el driver correcto
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

