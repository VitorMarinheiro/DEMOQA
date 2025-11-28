from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.alert_frame_and_windows_page import AlertFrameAndWindowsPage
from pages.browser_windows_page import BrowserWindowsPage
import pytest

# Scenarios
scenarios('../features/alerts_frame_windows/browser_windows.feature')

# Fixtures
@pytest.fixture
def home_page(driver, config):
    return HomePage(driver, config)

@pytest.fixture
def alert_frame_and_windows_page(driver, config):
    return AlertFrameAndWindowsPage(driver, config)

@pytest.fixture
def browser_windows_page(driver, config):
    return BrowserWindowsPage(driver, config)

# Steps
@given('que eu esteja na página de Browser Windows')
def go_to_browser_windows_page(home_page, alert_frame_and_windows_page, browser_windows_page):
    home_page.go_to(home_page.config["base_url"])
    alert_frame_and_windows_page = home_page.click_windows_card()
    alert_frame_and_windows_page.validate_page_url()
    alert_frame_and_windows_page.click_browser_windows_menu()
    browser_windows_page.validate_page_url()

@when('eu abrir uma nova janela')
def open_new_window(browser_windows_page):
    browser_windows_page.open_new_window_and_validate_it()

@then('o conteúdo da nova janela deve ser validado com sucesso')
def validate_new_window_content(browser_windows_page):
    # A validação já é feita no método open_new_window_and_validate_it()
    # do Page Object. Este step serve para dar semântica ao cenário
    pass