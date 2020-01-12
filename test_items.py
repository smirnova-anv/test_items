import time

def test_add_to_cart_button_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary")
    assert button, 'Error: no button "Add to basket"'

