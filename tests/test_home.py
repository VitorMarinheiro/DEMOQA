import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver", "config")
class TestHome:
    """
    Test suite for the home page.
    """

    def test_page_title(self, driver, config):
        """
        Tests if the home page title is correct.
        """
        home_page = HomePage(driver)
        home_page.go_to(config["base_url"])
        title = home_page.get_tab_title()
        assert title == "DEMOQA"
