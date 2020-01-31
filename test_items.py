import pytest
import time

@pytest.mark.parametrize('language', ["en-gb", "fr"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket") .click()
    browser.implicitly_wait(30)
    text = browser.find_element_by_xpath('//strong[contains(text(), "Coders at Work")]').text
    assert text == "Coders at Work",\
        f"Got '{text}' as expected"
