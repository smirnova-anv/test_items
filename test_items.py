def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary")
    assert button, f'Error: {"no button"}'
