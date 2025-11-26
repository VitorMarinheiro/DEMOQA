from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

class WebDriverFactory:
    """
    Factory for creating WebDriver instances.
    """

    @staticmethod
    def get_driver(browser_name):
        """
        Returns a WebDriver instance based on the browser name.
        """
        if browser_name.lower() == "chrome":
            service = ChromeService(executable_path=ChromeDriverManager().install())
            return webdriver.Chrome(service=service)
        elif browser_name.lower() == "firefox":
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            return webdriver.Firefox(service=service)
        else:
            raise Exception(f"Navegador '{browser_name}' não é suportado.")
