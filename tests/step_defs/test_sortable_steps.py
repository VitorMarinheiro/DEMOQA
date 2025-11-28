from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.interactions_page import InteractionsPage
from pages.sortable_page import SortablePage
import pytest

# Scenarios
scenarios('../features/interactions/sortable.feature')

# Fixtures
@pytest.fixture
def home_page(driver, config):
    return HomePage(driver, config)

@pytest.fixture
def interactions_page(driver, config):
    return InteractionsPage(driver, config)

@pytest.fixture
def sortable_page(driver, config):
    return SortablePage(driver, config)

# Steps
@given('que eu esteja na página de Ordenação')
def go_to_sortable_page(home_page, interactions_page, sortable_page):
    home_page.go_to(home_page.config["base_url"])
    interactions_page = home_page.click_interaction_card()
    interactions_page.validate_page_url()
    interactions_page.click_sortable_menu()
    sortable_page.validate_page_url()

@when('eu ordenar os itens em ordem decrescente')
def sort_items_descending(sortable_page):
    sortable_page.sort_descending()

@then('os itens devem estar em ordem decrescente')
def items_should_be_in_descending_order(sortable_page):
    item_texts = sortable_page.get_item_texts()
    expected_order = ['Six', 'Five', 'Four', 'Three', 'Two', 'One']
    assert item_texts == expected_order, f"A lista não está em ordem decrescente. Ordem atual: {item_texts}"