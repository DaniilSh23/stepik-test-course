import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):
    '''
    Фикстура для запуска и остановки браузера,
    работает отдельно для каждой функции
    '''
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()