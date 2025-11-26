from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

class ProgressBarPage(BasePage):
    """
    Page Object for the Progress bar page.
    """
    _start_stop_button = (By.ID, "startStopButton")
    _progress_bar = (By.XPATH, "//*[@role='progressbar']")
    _reset_button = (By.ID, "resetButton")
 
    def __init__(self, driver, config):
        """
        Initializes the ProgressBarPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        """
        Validate page url comparing the actual page with the expected url.
        """
        assert f'{self.config["base_url"]}progress-bar' == self.get_current_url()

    def validate_progress_bar_stop(self):
        """
        Validate the progress bar start and stop before 25%
        """
        self._click(self._start_stop_button)
        time.sleep(1)
        self._click(self._start_stop_button)
        progress = self._get_property(self._progress_bar, "aria-valuenow")
        assert int(progress) <= 25, f"Progress bar is already after 25%. Actual value {progress}."
        
    def wait_for_progress_bar_to_complete(self, timeout=10):
        """
        Waits for the progress bar to reach 100%.
        :param timeout: The maximum time to wait for the progress bar to complete.
        """
        self.wait = WebDriverWait(self.driver, timeout)
        self.wait.until(
            lambda driver: self._get_property(self._progress_bar, "aria-valuenow") == "100"
        )

    def validate_progress_bar_finish(self):
        """
        Validate finish the progress bar
        """
        self._click(self._start_stop_button)
        self.wait_for_progress_bar_to_complete()
        progress = self._get_property(self._progress_bar, "aria-valuenow")
        assert int(progress) == 100, f"Progress bar did not reach 100%. Actual value {progress}."
        self._click(self._reset_button)