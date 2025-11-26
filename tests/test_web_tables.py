import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver", "config")
class TestWebTables:
    """
    Test suite for the web Tables pages.
    """

    def test_web_tables_flow(self, driver, config):
        """
        Tests the web tables flow.
        """
        home_page = HomePage(driver, config)
        home_page.validate_page_url()
        
        elements_page = home_page.click_elements_card()
        elements_page.validate_page_url()
        
        web_tables_page = elements_page.click_web_tables_menu()
        web_tables_page.add_a_new_register()
        web_tables_page.edit_register()
        web_tables_page.delete_register()
        web_tables_page.clean_search_box()
        web_tables_page.create_multiple_registers()
        web_tables_page.delete_all_multiple_registers()