from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.widgets_page import WidgetsPage
from pages.progress_bar_page import ProgressBarPage
import pytest

# Scenarios
scenarios('../features/widgets/progress_bar.feature')

# Fixtures
@pytest.fixture
def home_page(driver, config):
    return HomePage(driver, config)

@pytest.fixture
def widgets_page(driver, config):
    return WidgetsPage(driver, config)

@pytest.fixture
def progress_bar_page(driver, config):
    return ProgressBarPage(driver, config)

# Steps
@given('que eu esteja na página da Barra de Progresso')
def go_to_progress_bar_page(home_page, widgets_page, progress_bar_page):
    home_page.go_to(home_page.config["base_url"])
    widgets_page = home_page.click_widgets_card()
    widgets_page.validate_page_url()
    widgets_page.click_progress_bar_menu()
    progress_bar_page.validate_page_url()

@when('eu iniciar a barra de progresso')
def start_progress_bar(progress_bar_page):
    progress_bar_page.validate_progress_bar_finish()

@then('a barra de progresso deve atingir 100%')
def progress_bar_should_be_complete(progress_bar_page):
    # A validação já é feita no método validate_progress_bar_finish()
    # do Page Object. Este step serve para dar semântica ao cenário.
    pass