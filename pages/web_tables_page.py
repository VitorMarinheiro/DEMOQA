from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class WebTablesPage(BasePage):
    """
    Page Object for the WebTablesPage
    """
    _new_register_button = (By.ID, "addNewRecordButton")
    _first_name_input = (By.ID, "firstName")
    _last_name_input = (By.ID, "lastName")
    _user_email_input = (By.ID, "userEmail")
    _age_input = (By.ID, "age")
    _salary_input = (By.ID, "salary")
    _department_input = (By.ID, "department")
    _submit_button = (By.ID, "submit")
    
    _search_box_input = (By.ID, "searchBox")
    _search_box_button = (By.ID, "basic-addon2")
    
    _edit_icon = (By.XPATH, "//*[@Title='Edit']")
    _delete_icon = (By.XPATH, "//*[@Title='Delete']")
    _salary_cell = (By.XPATH, "//div[@class='rt-tr-group'][1]//div[@role='gridcell'][5]")
    _no_rows_found_message = (By.CLASS_NAME, "rt-noData")
    _first_row = (By.XPATH, "//div[@class='rt-tr-group'][1]")
    
    
    def __init__(self, driver, config):
        """
        Initializes the WebTablesPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        """
        Validate page url comparing the actual page with the expected url.
        """
        assert f'{self.config["base_url"]}webtables' == self.get_current_url()
        
    def add_a_new_register(self, firstName="Vitor", lastName="Marinheiro", email="vitor.marinheiro@test.com", age="30", salary="9999", department="IT"):
        """
        Adds a new register to the web table.
        """
        self._click(self._new_register_button)
        self._type(self._first_name_input, firstName)
        self._type(self._last_name_input, lastName)
        self._type(self._user_email_input, email)
        self._type(self._age_input, age)
        self._type(self._salary_input, salary)
        self._type(self._department_input, department)
        time.sleep(0.1)
        self._click(self._submit_button)
    
    def edit_register(self):
        """
        Edits an existing register in the web table.
        """
        time.sleep(0.5)
        self._type(self._search_box_input, "Vitor")
        time.sleep(0.1)
        self._click(self._edit_icon)
        self._clear(self._salary_input)
        self._type(self._salary_input, 1000)
        self._click(self._submit_button)
        
    def delete_register(self):
        """
        Deletes a register from the web table.
        """
        time.sleep(0.5)
        self._click(self._delete_icon)
        
    def clean_search_box(self):
        """
        Clears the search box.
        """
        self._clear(self._search_box_input)
        self._type(self._search_box_input, "a")
        self._clear(self._search_box_input)
        self._click(self._search_box_button)
        
    def create_multiple_registers(self):
        """
        Creates multiple registers in the web table.
        """
        for _ in range(11):
            self.add_a_new_register()
            time.sleep(0.1)
            
    def delete_all_multiple_registers(self):
        """
        Delete the multiple registers created in the web table.
        """
        time.sleep(0.5)
        self._type(self._search_box_input, "Vitor")
        time.sleep(0.1)
        for _ in range(11):
            self.delete_register()
            time.sleep(0.1)
            
    def search_for(self, text):
        self._clear(self._search_box_input)
        self._type(self._search_box_input, text)

    def get_salary_text(self):
        return self._get_text(self._salary_cell)

    def is_no_rows_message_displayed(self):
        return self.assert_element_is_visible(self._no_rows_found_message)

    def get_no_rows_message_text(self):
        return self._get_text(self._no_rows_found_message)

    def get_first_row_text(self):
        if self.is_element_present(self._first_row):
            return self._get_text(self._first_row)
        return None