from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user_wrongUN", "secret_sauce_wrongPW")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"    


def test_locked_out_user(page):
    login_page = LoginPage(page)    
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out."      

