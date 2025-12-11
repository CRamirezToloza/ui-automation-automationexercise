# 🧪 UI Automation – Automation Exercise (Selenium + Pytest + POM)

<table>
<tr>

<td width="50%" valign="top">

<h2 align="center">Versión en español</h2>

📌 Framework de automatización UI para:  
<a href="https://automationexercise.com" target="_blank">https://automationexercise.com</a>  

Este repositorio implementa un framework de automatización para pruebas smoke y flujos E2E.  
Está desarrollado con **Python, Selenium WebDriver y Pytest**, aplicando el patrón **Page Object Model (POM)** para mantener el código modular, legible y fácil de extender con nuevos casos de prueba.

### 🎯 Objetivos del proyecto
- Automatizar flujos críticos de la aplicación
- Aplicar buenas prácticas:
  - Esperas explícitas  
  - Manipulación de overlays  
  - Scroll automático para evitar *click interceptions*  
  - Reutilización de métodos para escalabilidad  
  - Tests parametrizables  
  - Selectores CSS estables (sin uso de textos ni índices frágiles)
    
### 🧪 Test Cases Incluidos

#### 🔐 Login
- **TC01 – Login exitoso:**  
  Verifica que un usuario registrado pueda iniciar sesión correctamente.
- **TC02 – Login con credenciales inválidas:**  
  Valida la visualización del mensaje de error ante credenciales incorrectas.

#### 🛒 Carrito de Compras (Cart)
- **TC10 – Agregar primer producto al carrito:**  
  Hover → Mostrar overlay → Clic en “Add to Cart” → Validar modal → Ir al carrito.
- **TC12 – Agregar múltiples productos al carrito:**  
  - Hover + clic en varios productos  
  - Manejo del modal (“Continue Shopping”)  
  - Validación en carrito: precios, cantidades y totales  
  - Cálculo automático `price * qty = total`

### 🧼 Pruebas de interfaz
- Validación de visibilidad de elementos.
- Validación de navegación entre páginas.
- Manejo de overlays y elementos dinámicos.
    

</td>

<td width="50%" valign="top">

<h2 align="center">English version</h2>

📌 UI Test Automation Framework for:  
<a href="https://automationexercise.com" target="_blank">https://automationexercise.com</a>  

This repository implements an automation framework for smoke tests and end-to-end (E2E) flows.  
It is built using **Python, Selenium WebDriver, and Pytest**, following the **Page Object Model (POM)** to keep the code modular, readable, and easy to extend with new test cases.

### 🎯 Project Objectives
- Automate critical application flows:
- Apply best practices:
  - Explicit waits  
  - Overlay handling  
  - Automatic scrolling to avoid click interception  
  - Reusable methods for scalability  
  - Parametrized tests  
  - Stable CSS selectors (avoiding fragile text-based or index-based locators)
    

### 🧪 Included Test Cases 

#### 🔐 Login
- **TC01 – Successful login:**  
  Verifies that a registered user can log in correctly.
- **TC02 – Login with invalid credentials:**  
  Validates that the correct error message is displayed when credentials are incorrect.

#### 🛒 Shopping Cart
- **TC10 – Add first product to cart:**  
  Hover → Display overlay → Click “Add to Cart” → Validate modal → Navigate to cart.
- **TC12 – Add multiple products to cart:**  
  - Hover + click on multiple products 
  - Modal handling (“Continue Shopping”)  
  - Cart validation: prices, quantities, totals
  - Automatic calculation `price * qty = total`

### 🧼 UI Checks
- Element visibility validation.
- Page navigation validation.
- Handling of overlays and dynamic elements.

</td>
</tr>
</table>

---

## 🛠 Tecnologías / Tools

- Python 3.13  
- Selenium WebDriver  
- Pytest  
- Page Object Model (POM)  
- Git / GitHub  

*(Próximas mejoras: reportes pytest-html, ejecución en CI/CD con GitHub Actions, Allure Reports, más flujos E2E)*  
*(Coming improvements: pytest-html reporting, CI/CD execution with GitHub Actions, Allure Reports, additional E2E flows)*

---

## 📁 Estructura del proyecto / Project Structure

```text
ui-automation-automationexercise/
├── README.md
├── requirements.txt
├── conftest.py
├── tests/
│   ├── test_login.py
│   └── test_add_to_cart.py
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── cart_page.py
└── utils/
    ├── configuration.py
    └── helpers.py
