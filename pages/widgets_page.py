from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.progress_bar_page import ProgressBarPage

class WidgetsPage(BasePage):
    """
    Page Object for the Widgets page.
    """
    _progress_bar_menu = (By.XPATH, "//span[text()='Progress Bar']")
 
    def __init__(self, driver, config):
        """
        Initializes the WidgetsPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        assert f'{self.config["base_url"]}widgets' == self.get_current_url()
        
    def click_progress_bar_menu(self):
        """
        Clicks the 'Progress Bar' card on the widgets page.
        """
        self.scroll_to_element(self._progress_bar_menu)
        self._click(self._progress_bar_menu)
        return ProgressBarPage(self.driver, self.config)