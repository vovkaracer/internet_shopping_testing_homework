from selenium.webdriver.common.by import By

def test_user_should_see_button_to_add_to_shopping_cart(browser):
    browser.implicitly_wait(5)
    button_to_add_to_shopping_card = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert bool(button_to_add_to_shopping_card), "There is no add to cart button"
