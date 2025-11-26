from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.sortable_page import SortablePage

class InteractionsPage(BasePage):
    """
    Page Object for the interactions page.
    """

    _sortable_menu = (By.XPATH, "//span[text()='Sortable']")
 
    def __init__(self, driver, config):
        """
        Initializes the InteractionsPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        assert f'{self.config["base_url"]}interaction' == self.get_current_url()
        
    def click_sortable_menu(self):
        """
        Clicks the 'Sortable' card on the Interactions page.
        """
        self._click(self._sortable_menu)
        return SortablePage(self.driver, self.config)