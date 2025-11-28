import pytest
from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.forms_page import FormsPage
from pages.practice_form_page import PracticeFormsPage

# Scenarios
scenarios('../features/forms/practice_form.feature')

# Fixtures
@pytest.fixture
def home_page(driver, config):
    return HomePage(driver, config)

@pytest.fixture
def forms_page(driver, config):
    return FormsPage(driver, config)

@pytest.fixture
def practice_forms_page(driver, config):
    return PracticeFormsPage(driver, config)

# Steps
@given('que eu esteja na página inicial')
def initial_page(home_page):
    home_page.validate_page_url()

@when('eu navegar para a página de formulário de prática')
def navigate_to_practice_form(home_page, forms_page):
    forms_page = home_page.click_forms_card()
    forms_page.validate_page_url()
    forms_page.click_practice_forms_menu()


@when('eu preencher o formulário com dados válidos')
def fill_the_form(practice_forms_page):
    practice_forms_page.validate_page_url()
    practice_forms_page.fill_form()

@then('eu devo ver um popup de confirmação com os dados submetidos')
def validate_popup(practice_forms_page):
    practice_forms_page.validate_popup()