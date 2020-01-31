import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome")
    parser.addoption('--language', action='store',default='chrome',
                     help="Choose language:ru,en,..(etc.)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'user_language'})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(7)
    else:
        raise pytest.UsageError("--browser_name should be chrome")
    yield browser
    print("\nquit browser..")
    browser.quit()
