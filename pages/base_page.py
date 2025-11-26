from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Base class for all Page Objects.
    Contains common methods for interacting with the page.
    """

    def __init__(self, driver):
        """
        Initializes the BasePage with the Selenium driver.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def _find(self, locator):
        """
        Finds an element on the page.
        """
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        """
        Clicks an element on the page.
        """
        self.wait.until(EC.element_to_be_clickable((locator["by"], locator["value"])))
        self._find(locator).click()

    def _type(self, locator, text):
        """
        Types text into an element.
        """
        self.wait.until(EC.visibility_of_element_located((locator["by"], locator["value"])))
        self._find(locator).send_keys(text)

    def _get_text(self, locator):
        """
        Gets the text of an element.
        """
        self.wait.until(EC.visibility_of_element_located((locator["by"], locator["value"])))
        return self._find(locator).text

    def get_current_url(self):
        """
        Returns the current URL of the page.
        """
        return self.driver.current_url
    
    def get_tab_title(self):
        """
        Returns the current title of the page.
        """
        self.wait.until(lambda driver: driver.title != "")
        return self.driver.title