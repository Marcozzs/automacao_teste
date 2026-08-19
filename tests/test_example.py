from pages.login_page import LoginPage
from playwright.sync_api import Page, Locator
def test_login_accepeted(page: Page):
    # 1. Acessa a página de teste de login
    page.goto("https://www.saucedemo.com")
    # 2. Instancia a Page Object 
    login_page = LoginPage(page)
    # 3. Executa a ação de login mapeada na classe
    login_page.login("standard_user", "secret_sauce")
    login_page.
    
    # 4. Validação simples para garantir que a ação ocorreu (mudou de URL)
    assert "inventory.html" in page.url
    print("\nValidação OK: Login com sucesso!")
    
def test_login_password_invalid(page: Page):
    page.goto("https://www.saucedemo.com")
    login_page = LoginPage(page)
    login_page.login("standard_user", "@#$@")
    
    # Validação do bloco de erro
    error_message: Locator = page.locator("[data-test='error']")
    texto_erro = error_message.inner_text()
    assert "Epic sadface: Username and password do not match any user in this service" in texto_erro
    print(f"\nValidação OK: Mensagem capturada -> '{texto_erro}'")

def test_login_password_empty(page: Page):
    page.goto("https://www.saucedemo.com")
    login_page = LoginPage(page)
    login_page.login("standard_user", "")
    
    # Validação do bloco de erro
    error_message: Locator = page.locator("[data-test='error']")
    texto_erro = error_message.inner_text()
    assert "Epic sadface: Password is required" in texto_erro
    print(f"\nValidação OK: Mensagem capturada -> '{texto_erro}'")