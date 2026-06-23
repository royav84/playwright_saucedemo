def test_valid_login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_invalid_login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user_wrongUN")
    page.fill("#password", "secret_sauce_wrongPW")
    page.click("#login-button")
    assert page.locator("[data-test='error']").is_visible()
