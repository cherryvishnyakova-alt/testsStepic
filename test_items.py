import time


def test_add_to_cart_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    time.sleep(30)  # для визуальной проверки
    
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена"
