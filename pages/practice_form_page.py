from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from pathlib import Path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class PracticeFormsPage(BasePage):
    """
    Page Object for the practice forms page.
    """

    _first_name_input = (By.ID, "firstName")
    _last_name_input = (By.ID, "lastName")
    _user_email_input = (By.ID, "userEmail")
    
    # GENDER
    _gender_radio = (By.XPATH, "//*[text()='gender']")
    
    _user_number_input = (By.ID, "userNumber")
    _date_of_birth_input = (By.ID, "dateOfBirthInput")
    
    # DATE PICKED
    _date_of_birth_year_select = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    _date_of_birth_month_select = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    _date_of_birth_day_div = (By.XPATH, "//div[text()='day']")
    
    _subject_input = (By.ID, "subjectsInput")
    
    # HOBBIES
    _hobbies_sports_check = (By.XPATH, "//*[text()='Sports']")
    _hobbies_reading_check = (By.XPATH, "//*[text()='Reading']")
    _hobbies_music_check = (By.XPATH, "//*[text()='Music']")
    
    _current_address_input = (By.ID, "currentAddress")
    
    _state_select = (By.ID, "react-select-3-input")
    _city_select = (By.ID, "react-select-4-input")
    
    _upload_picture_button = (By.ID, "uploadPicture")
    
    _submit_button = (By.ID, "submit")
        
    # Validation
    _validation_form = (By.XPATH, "//*[text()='Thanks for submitting the form']")
    _close_popup_button = (By.ID, "closeLargeModal")
 
    def __init__(self, driver, config):
        """
        Initializes the PracticeFormsPage.
        """
        super().__init__(driver)
        self.config = config

    def validate_page_url(self):
        """
        Validate page url comparing the actual page with the expected url.
        """
        assert f'{self.config["base_url"]}automation-practice-form' == self.get_current_url()
        
    def select_value_from_date_picker(self, locator, value):
        """
        Select a date from date picker
        
        Args:
            locator: Locator from element to be used
            value: ("January", "2025", ...) OR number (0-11)
        """
        select = Select(self._find(locator))
        
        # detect the input type
        if isinstance(value, str):
            select.select_by_visible_text(value)
        else:
            select.select_by_value(str(value))
        
        time.sleep(0.3)
        
    def scroll_to_element(self, locator):
        """
        Scroll down to an element using a padding of 350px.
        """
        y = self._find(locator).location['y']
        self.driver.execute_script(f"window.scrollTo(0, {y - 350});")
        time.sleep(1)
        
    def _read_input_data(self):
        """
        Reads the input data from the input_values.txt file.
        """
        data = {}
        file_path = Path(__file__).resolve().parent.parent / "data" / "input_values.txt"
        with open(file_path, 'r') as file:
            for line in file:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    data[key.strip()] = value.strip()
        return data

    def fill_form(self):
        """
        Fills the practice form with data from input_values.txt
        """
        form_data = self._read_input_data()

        # Name
        self._type(self._first_name_input, form_data['first_name'])
        self._type(self._last_name_input, form_data['last_name'])
        
        # Email
        self._type(self._user_email_input, form_data['user_email'])
        
        # Gender
        if form_data['gender'].strip().capitalize() in ['Male', 'Female', 'Other']:
            self._click((self._gender_radio[0], (self._gender_radio[1]).replace("gender", form_data['gender'].strip().capitalize())))
        else:
            assert False, f"Invalid Gender: {form_data['gender'].strip().capitalize()}"
            
        # Mobile
        self._type(self._user_number_input, form_data['user_number'])
        
        # Date of Birth
        self._click(self._date_of_birth_input)
        time.sleep(0.2)
        self.select_value_from_date_picker(self._date_of_birth_year_select, form_data['birth_year'])
        self.select_value_from_date_picker(self._date_of_birth_month_select, form_data['birth_month'])
        self._click((self._date_of_birth_day_div[0], (self._date_of_birth_day_div[1]).replace("day", form_data['birth_day'])))
        
        # Subjects
        self._click(self._subject_input)
        self._type(self._subject_input, form_data['subject'])
        time.sleep(0.2)
        self._type(self._subject_input, Keys.ENTER)
        
        # Hobbies
        self.scroll_to_element(self._hobbies_sports_check)
        if "sports" in form_data['hobbies'].lower():
            self._click(self._hobbies_sports_check)
        if "reading" in form_data['hobbies'].strip().capitalize():
            self._click(self._hobbies_reading_check)
        if "music" in form_data['hobbies'].strip().capitalize():
            self._click(self._hobbies_music_check)
        
        # Picture
        _image_path = str(Path(__file__).resolve().parent.parent / "data" / form_data['image'])
        self._type(self._upload_picture_button, _image_path)

        # Current Address
        self._type(self._current_address_input, form_data['current_address'])

        # State 
        self.driver.execute_script("arguments[0].click();", self._find(self._state_select))
        time.sleep(0.2)
        self._type(self._state_select, form_data['state'])
        time.sleep(0.2)
        self._type(self._state_select, Keys.ENTER)
        
        # City
        self.driver.execute_script("arguments[0].click();", self._find(self._city_select))
        time.sleep(0.2)
        self._type(self._city_select, form_data['city'])
        time.sleep(0.2)
        self._type(self._city_select, Keys.ENTER)

        # Submit
        self.scroll_to_element(self._submit_button)
        self._click(self._submit_button)
        
        
    def validate_popup(self):
        """
        Validate the pop up after submiting the form.
        """
        self.assert_element_is_visible(self._validation_form)
        self._click(self._close_popup_button)
        self.assert_element_is_not_visible(self._validation_form)
        