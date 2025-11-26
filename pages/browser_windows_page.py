from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from pathlib import Path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class BrowserWindowsPage(BasePage):
    """
    Page Object for the BrowserWindowsPage
    """
    _new_window_button = (By.ID, "windowButton")
    _window_title = (By.ID, "sampleHeading")
    
    def __init__(self, driver, config):
        """
        Initializes the PracticeFormsPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        """
        Validate page url comparing the actual page with the expected url.
        """
        assert f'{self.config["base_url"]}browser-windows' == self.get_current_url()
        
    def open_new_window_and_validate_it(self):
        """
        Click on 'New Window' button and validate the new window title
        """
        original_window = self.driver.current_window_handle
        self._click(self._new_window_button)
        time.sleep(0.5)
        
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.assert_element_is_visible(self._window_title)
        
        # Close and go back to the original window
        self.driver.close()
        self.driver.switch_to.window(original_window)