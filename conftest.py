import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: en, es, fr, de, ru, etc.'
    )


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    
    chrome_options = Options()
    chrome_options.add_argument('--lang=' + language)
    
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(5)
    
    yield browser
    browser.quit()
