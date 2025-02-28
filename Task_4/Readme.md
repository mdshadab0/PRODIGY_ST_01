
# Cross-Browser Testing with BrowserStack and Selenium

This project demonstrates cross-browser testing using BrowserStack and Selenium WebDriver. It allows automated testing of a demo website across multiple browsers and operating systems without the need to manually set up environments.

## Prerequisites

Before running the tests, make sure you have the following installed:

- Python 3.7+
- Pip (Python package installer)
- BrowserStack account (you can sign up [here](https://www.browserstack.com/users/sign_up))

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/cross-browser-testing-with-browserstack.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cross-browser-testing-with-browserstack
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your BrowserStack credentials:
   - Replace the placeholder values in the script with your **BrowserStack username** and **access key**.
   - You can find your credentials on the BrowserStack [Automate Dashboard](https://www.browserstack.com/automate).

5. (Optional) You can set your credentials as environment variables instead of hardcoding them in the script:

   ```bash
   export BROWSERSTACK_USERNAME="your_browserstack_username"
   export BROWSERSTACK_ACCESS_KEY="your_browserstack_access_key"
   ```

## Running the Tests

1. After setting up your credentials, you can run the tests across multiple browsers by executing the script:

   ```bash
   python 'Cross-Browser testing with BrowserStack.py'
   ```

   The test will:
   - Open the SauceDemo login page.
   - Log in using the provided credentials.
   - Perform the login test on Chrome, Firefox, Safari, and Edge.

2. You can view the results of the test (including logs, screenshots, and video recordings) on your [BrowserStack Automate Dashboard](https://automate.browserstack.com/).

## Demo Site Credentials

The tests are run against the [SauceDemo](https://www.saucedemo.com/) website. Here are the credentials used in the test:

- **Username**: `standard_user`
- **Password**: `secret_sauce`

## Customization

You can easily modify the `browsers` list in the script to add or remove browsers and operating systems. Refer to the [BrowserStack capabilities](https://www.browserstack.com/automate/capabilities) to customize the configurations.

## Example

Here’s an example of how the output looks in the terminal after running the test:

```bash
Login Successful on Chrome - Page Title: Swag Labs
Login Successful on Firefox - Page Title: Swag Labs
Login Successful on Safari - Page Title: Swag Labs
Login Successful on Edge - Page Title: Swag Labs
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
