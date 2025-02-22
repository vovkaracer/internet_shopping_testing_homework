from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    link = f'https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print('\nquit browser')
    browser.quit()