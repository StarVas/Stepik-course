import time

def test_add_to_cart_button_is_displayed(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket") .click()
    text = browser.find_element_by_xpath('//strong[contains(text(), "Coders at Work")]').text
    assert text == "Coders at Work",\
        f"Got '{text}' as expected"
