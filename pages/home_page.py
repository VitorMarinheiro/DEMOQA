from pages.base_page import BasePage
from pages.forms_page import FormsPage
from pages.alert_frame_and_windows_page import AlertFrameAndWindowsPage
from pages.elements_page import ElementsPage
from pages.widgets_page import WidgetsPage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    """
    Page Object for the home page.
    """

    _forms_card = (By.XPATH, "//h5[text()='Forms']")
    _windows_card = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
    _elements_card = (By.XPATH, "//h5[text()='Elements']")
    _widgets_card = (By.XPATH, "//h5[text()='Widgets']")
 
    def __init__(self, driver, config):
        """
        Initializes the HomePage.
        """
        super().__init__(driver)
        self.config = config
        self.driver.get(self.config["base_url"])
        
    def go_to(self, url):
        """
        Navigates to the home page URL.
        """
        self.driver.get(url)

    def click_forms_card(self):
        """
        Clicks the 'Forms' card on the home page.
        """
        self._click(self._forms_card)
        return FormsPage(self.driver, self.config)
    
    def click_windows_card(self):
        """
        Clicks the 'Alerts, Frame & Windows' card on the home page.
        """
        self._click(self._windows_card)
        return AlertFrameAndWindowsPage(self.driver, self.config)

    def click_elements_card(self):
        """
        Clicks the 'Elements' card on the home page.
        """
        self._click(self._elements_card)
        return ElementsPage(self.driver, self.config)
    
    def click_widgets_card(self):
        """
        Clicks the 'Widgets' card on the home page.
        """
        self._click(self._widgets_card)
        return WidgetsPage(self.driver, self.config)

    def validate_page_url(self):
        assert f'{self.config["base_url"]}' == self.get_current_url()
        