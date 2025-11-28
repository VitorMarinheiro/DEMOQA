import pytest
from pages.home_page import HomePage
import time

@pytest.mark.sortable
@pytest.mark.usefixtures("driver", "config")
class TestSortable:
    """
    Test suite for the sortable pages.
    """

    def test_sortable_flow(self, driver, config):
        """
        Tests the sortable flow.
        """
        home_page = HomePage(driver, config)
        home_page.validate_page_url()
        
        interactions_page = home_page.click_interaction_card()
        interactions_page.validate_page_url()
        
        sortable_page = interactions_page.click_sortable_menu()
        sortable_page.sort_descending()