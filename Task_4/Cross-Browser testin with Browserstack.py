from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Your BrowserStack credentials
BROWSERSTACK_USERNAME = 'shadab_Akg9CJ'
BROWSERSTACK_ACCESS_KEY = 'DYpxttYPYR62ghf4HVyQ'

# List of desired capabilities for different browsers
browsers = [
    {
        'browser': 'Chrome',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'browserVersion': 'latest',
            'sessionName': 'Cross-Browser Login Test on Chrome (Windows)',
        }
    },
    {
        'browser': 'Firefox',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'browserVersion': 'latest',
            'sessionName': 'Cross-Browser Login Test on Firefox (Windows)',
        }
    },
    {
        'browser': 'Safari',
        'bstack:options': {
            'os': 'OS X',
            'osVersion': 'Monterey',
            'browserVersion': 'latest',
            'sessionName': 'Cross-Browser Login Test on Safari (macOS)',
        }
    },
    {
        'browser': 'Edge',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'browserVersion': 'latest',
            'sessionName': 'Cross-Browser Login Test on Edge (Windows)',
        }
    }
]

# Function to set the correct options object based on the browser type
def get_browser_options(browser_name, browser_config):
    if browser_name == 'Chrome':
        options = webdriver.ChromeOptions()
    elif browser_name == 'Firefox':
        options = webdriver.FirefoxOptions()
    elif browser_name == 'Safari':
        options = webdriver.SafariOptions()
    elif browser_name == 'Edge':
        options = webdriver.EdgeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Set the bstack:options capabilities for BrowserStack
    options.set_capability('bstack:options', browser_config['bstack:options'])
    
    return options

# Function to run the test on a given browser configuration
def run_test(browser_config):
    driver = None
    try:
        # Initialize WebDriver for BrowserStack with correct options
        browser_name = browser_config['browser']
        options = get_browser_options(browser_name, browser_config)

        driver = webdriver.Remote(
            command_executor=f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub',
            options=options  # Pass the correct browser options
        )

        # Open SauceDemo login page
        driver.get("https://www.saucedemo.com/")

        # Find the username input field and enter the username
        username_input = driver.find_element("id", "user-name")
        username_input.send_keys("standard_user")  # Using a valid username

        # Find the password input field and enter the password
        password_input = driver.find_element("id", "password")
        password_input.send_keys("secret_sauce")  # Using the valid password

        # Find the login button and click it
        login_button = driver.find_element("id", "login-button")
        login_button.click()

        # Check if the login was successful
        print(f"Login Successful on {browser_config['browser']} - Page Title: " + driver.title)

    except WebDriverException as e:
        print(f"Test failed on {browser_config['browser']}: {e}")
    finally:
        if driver is not None:
            # Close the browser after the test
            driver.quit()

# Loop through the browser configurations and run the test
for browser in browsers:
    run_test(browser)
