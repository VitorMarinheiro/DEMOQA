from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    """
    Page Object for the home page.
    """

    def __init__(self, driver):
        """
        Initializes the HomePage.
        """
        super().__init__(driver)
        

    def go_to(self, url):
        """
        Navigates to the home page URL.
        """
        self.driver.get(url)
