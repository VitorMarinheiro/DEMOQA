# Web Test Automation Project with Selenium and Python

This project contains automated tests for the DEMOQA web application, using Behavior-Driven Development (BDD) with `pytest-bdd` and the Page Object design pattern to organize UI elements and interactions.

## Technologies Used

*   **Language:** Python
*   **Browser Automation:** Selenium
*   **Test Framework:** pytest
*   **WebDriver Management:** webdriver-manager
*   **Reports:** pytest-html

## Project Structure

The project structure is organized as follows:

- `config/`: Configuration files (URLs, credentials, etc.).
- `data/`: Test data files.
- `features/`: Feature files written in Gherkin (`.feature`).
- `pages/`: Page Object classes, which represent the application pages.
- `reports/`: Test execution reports.
- `tests/`: Test scripts, including step definitions for BDD scenarios.
- `utils/`: Utility functions and classes.

## Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:VitorMarinheiro/DEMOQA.git
    cd DEMOQA
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
```

### Running Tests by Tag

You can run specific tests by using markers (tags). The available markers are defined in the `pytest.ini` file.

To run tests with a specific tag, use the `-m` option with `pytest`. For example, to run only the tests tagged as `web_tables`:

```bash
pytest -m "web_tables" --html=reports/report.html
```

Here are the available tags:

- `browser_windows`
- `bookstore_api`
- `web_tables`
- `practice_form`
- `sortable`
- `progress_bar`
