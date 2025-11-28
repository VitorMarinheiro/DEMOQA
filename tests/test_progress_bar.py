import pytest
from pages.home_page import HomePage

@pytest.mark.progress_bar
@pytest.mark.usefixtures("driver", "config")
class TestProgressBar:
    """
    Test suite for the Progress Bar page.
    """

    def test_progress_bar_flow(self, driver, config):
        """
        Tests the progress bar flow.
        """
        home_page = HomePage(driver, config)
        home_page.validate_page_url()
        
        widgets_page = home_page.click_widgets_card()
        widgets_page.validate_page_url()
        
        progress_bar_page = widgets_page.click_progress_bar_menu()
        progress_bar_page.validate_progress_bar_stop()
        progress_bar_page.validate_progress_bar_finish()