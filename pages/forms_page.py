from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.practice_form_page import PracticeFormsPage

class FormsPage(BasePage):
    """
    Page Object for the forms page.
    """

    _practice_forms_menu = (By.XPATH, "//span[text()='Practice Form']")
 
    def __init__(self, driver, config):
        """
        Initializes the FormsPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        assert f'{self.config["base_url"]}forms' == self.get_current_url()
        
    def click_practice_forms_menu(self):
        """
        Clicks the 'Practice Forms' card on the forms page.
        """
        self._click(self._practice_forms_menu)
        return PracticeFormsPage(self.driver, self.config)