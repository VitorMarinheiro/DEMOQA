import pytest
from pages.home_page import HomePage
import time

@pytest.mark.usefixtures("driver", "config")
class TestHome:
    """
    Test suite for the home page.
    """

    def test_practice_form(self, driver, config):
        """
        Tests the practice_from flow.
        """
        home_page = HomePage(driver, config)
        home_page.validate_page_url()
        
        forms_page = home_page.click_forms_card()
        forms_page.validate_page_url()
        
        practice_froms_page = forms_page.click_practice_forms_menu()
        practice_froms_page.validate_page_url()
        practice_froms_page.fill_form()
        practice_froms_page.validate_popup()