from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
from pages.elements_page import ElementsPage
from pages.web_tables_page import WebTablesPage
from selenium.webdriver.common.by import By
import pytest
import csv
import io

# Scenarios
scenarios('../features/elements/web_tables.feature')

# Fixtures
@pytest.fixture
def home_page(driver, config):
    return HomePage(driver, config)

@pytest.fixture
def elements_page(driver, config):
    return ElementsPage(driver, config)

@pytest.fixture
def web_tables_page(driver, config):
    return WebTablesPage(driver, config)

# Steps for the first scenario
@given('que eu esteja na página de Web Tables')
def go_to_web_tables_page(home_page, elements_page, web_tables_page):
    home_page.go_to(home_page.config["base_url"])
    elements_page = home_page.click_elements_card()
    elements_page.validate_page_url()
    elements_page.click_web_tables_menu()
    web_tables_page.validate_page_url()

@when('eu adicionar um novo registro')
def add_new_register(web_tables_page):
    web_tables_page.add_a_new_register()

@when('eu editar o registro recém-adicionado')
def edit_register(web_tables_page):
    web_tables_page.edit_register()

@then('o registro deve ser atualizado com sucesso')
def verify_register_updated(web_tables_page):
    web_tables_page.search_for("Vitor")
    assert web_tables_page.get_salary_text() == "1000"

@when('eu excluir o registro')
def delete_register(web_tables_page):
    web_tables_page.delete_register()

@then('o registro não deve mais existir na tabela')
def verify_register_deleted(web_tables_page):
    web_tables_page.search_for("Vitor")
    web_tables_page.is_no_rows_message_displayed()
    assert "No rows found" in web_tables_page.get_no_rows_message_text()
    web_tables_page.clean_search_box()
