import pytest
from pages.home_page import HomePage
import time

@pytest.mark.usefixtures("driver", "config")
class TestWindow:
    """
    Test suite for the windows pages.
    """

    def test_windows_flow(self, driver, config):
        """
        Tests the windows flow.
        """
        home_page = HomePage(driver, config)
        home_page.validate_page_url()
        
        alert_frame_and_windows_page = home_page.click_windows_card()
        alert_frame_and_windows_page.validate_page_url()
        
        browser_windows_page = alert_frame_and_windows_page.click_browser_windows_menu()
        browser_windows_page.open_new_window_and_validate_it()