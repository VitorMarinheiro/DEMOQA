from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.web_tables_page import WebTablesPage

class ElementsPage(BasePage):
    """
    Page Object for the Elements page.
    """

    _web_tables_menu = (By.XPATH, "//span[text()='Web Tables']")
 
    def __init__(self, driver, config):
        """
        Initializes the ElementsPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        assert f'{self.config["base_url"]}elements' == self.get_current_url()
        
    def click_web_tables_menu(self):
        """
        Clicks the 'Web Tables' card on the Elements page.
        """
        self._click(self._web_tables_menu)
        return WebTablesPage(self.driver, self.config)