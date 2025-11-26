from pages.base_page import BasePage
from pages.forms_page import FormsPage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    """
    Page Object for the home page.
    """

    _forms_card = (By.XPATH, "//h5[text()='Forms']")
 
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

    def validate_page_url(self):
        assert f'{self.config["base_url"]}' == self.get_current_url()
        