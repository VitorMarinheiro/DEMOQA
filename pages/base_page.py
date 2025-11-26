from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

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
        return self.driver.find_element(*locator)

    def _click(self, locator):
        """
        Clicks an element on the page.
        """
        self.wait.until(EC.element_to_be_clickable(locator))
        self._find(locator).click()

    def _type(self, locator, text):
        """
        Types text into an element.
        """
        self.wait.until(EC.visibility_of_element_located(locator))
        self._find(locator).send_keys(text)

    def _clear(self, locator):
        """
        Clear text from an input element.
        """
        self.wait.until(EC.visibility_of_element_located(locator))
        self._find(locator).clear()
    
    def _get_text(self, locator):
        """
        Gets the text of an element.
        """
        self.wait.until(EC.visibility_of_element_located(locator))
        return self._find(locator).text
    
    def _get_property(self, locator, property):
        """
        Gets the property of an element.
        """
        self.wait.until(EC.visibility_of_element_located(locator))
        return self._find(locator).get_attribute(property)

    def scroll_to_element(self, locator):
        """
        Scroll down to an element using a padding of 350px.
        """
        y = self._find(locator).location['y']
        self.driver.execute_script(f"window.scrollTo(0, {y - 350});")
        time.sleep(1)
        
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
    
    def assert_element_is_visible(self, locator):
        """
        Asserts that an element is visible on the page within a given timeout.
        Fails the test if the element is not visible.
        :param locator: The locator of the element to find.
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            assert False, f"Element with locator '{locator}' was not visible on the page within 10 seconds."

    def assert_element_is_not_visible(self, locator):
        """
        Asserts that an element is not visible on the page within a given timeout.
        Fails the test if the element is still visible.
        :param locator: The locator of the element.
        """
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            assert False, f"Element with locator '{locator}' was still visible on the page after 10 seconds."