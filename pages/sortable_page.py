from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class SortablePage(BasePage):
    """
    Page Object for the sortable page.
    """
    _elements_div = (By.XPATH, "//div[contains(@class, 'vertical-list-container mt-4')]/div")
    
 
    def __init__(self, driver, config):
        """
        Initializes the SortablePage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        """
        Validate page url comparing the actual page with the expected url.
        """
        assert f'{self.config["base_url"]}sortable' == self.get_current_url()
   
    def sort_descending(self):
        """
        Sorts the list of elements in descending order.
        """
        
        # Get original Order
        time.sleep(4)
        self.scroll_to_element(self._elements_div)
        print("=" * 50)
        print("Original Order")
        print("=" * 50)
        itens = self._finds(self._elements_div)
        for i, item in enumerate(itens):
            print(f"  Position {i+1}: {item.text}")
        
        # Revert
        print("\n" + "=" * 50)
        print("Reverting...")
        print("=" * 50)
        
        actions = ActionChains(self.driver)
        
        for movements in range(5):
            # Update the list
            itens = self._finds(self._elements_div)
            
            start = itens[-1]
            stop = itens[movements]
            
            # Drag and drop
            actions.click_and_hold(start).perform()
            time.sleep(0.3)
            
            actions.move_to_element(stop).perform()
            time.sleep(0.3)
            
            actions.release().perform()
            time.sleep(0.5)
            
            print(f"  ✓ Movement {movements+1}/5 done")
        