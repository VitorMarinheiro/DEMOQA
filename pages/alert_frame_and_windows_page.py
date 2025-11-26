from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.browser_windows_page import BrowserWindowsPage

class AlertFrameAndWindowsPage(BasePage):
    """
    Page Object for the AlertFrameAndWindows page.
    """

    _browser_windows_menu = (By.XPATH, "//span[text()='Browser Windows']")
 
    def __init__(self, driver, config):
        """
        Initializes the AlertFrameAndWindowsPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        assert f'{self.config["base_url"]}alertsWindows' == self.get_current_url()
        
    def click_browser_windows_menu(self):
        """
        Clicks the 'Browser Windows' card on the forms page.
        """
        self._click(self._browser_windows_menu)
        return BrowserWindowsPage(self.driver, self.config)