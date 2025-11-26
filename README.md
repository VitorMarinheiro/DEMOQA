# Web Test Automation Project with Selenium and Python

This project contains automated tests for the DEMOQA web application. It uses the Page Object design pattern to organize UI elements and interactions.

## Technologies Used

*   **Language:** Python
*   **Browser Automation:** Selenium
*   **Test Framework:** pytest
*   **WebDriver Management:** webdriver-manager
*   **Reports:** pytest-html

## Project Structure

The project structure is organized as follows:

- `config/`: Configuration files (URLs, credentials, etc.).
- `pages/`: Page Object classes, which represent the application pages.
- `reports/`: Test execution reports.
- `tests/`: Test scripts.
- `utils/`: Utility functions and classes.

## Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone 
    cd 
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Tests

To run all tests, use `pytest`. The command below will run the tests and generate an HTML report in the `reports/` folder.

```bash
pytest --html=reports/report.html
