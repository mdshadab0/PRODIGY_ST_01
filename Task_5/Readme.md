
# E-commerce Website Automated Checkout Script

This project automates the process of adding a product to the cart on an e-commerce demo website ([automationpractice.pl](http://www.automationpractice.pl/index.php)) by changing the size and color of the product and completing the checkout process. The script uses Selenium WebDriver for browser automation.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Google Chrome
- ChromeDriver (handled automatically by `webdriver_manager`)

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/ecommerce-automation.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ecommerce-automation
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Set up your environment variables for credentials:

   ```bash
   export USER_EMAIL="your_email"
   export USER_PASSWORD="your_password"
   ```

## Script Workflow

1. Opens the **Dresses** section of the website.
2. Applies the **In Stock** filter.
3. Selects a product by clicking on the product name.
4. Iterates through available color and size combinations:
   - Tries each color and size (S, M, L).
   - If a valid combination is found (in stock), the script adds the item to the cart.
5. Completes the checkout process by logging in with the provided credentials:
   - **Email**: `mdshadba0500@gmail.com`
   - **Password**: `Shadb@123`
6. Proceeds through checkout, including confirmation of the address, agreement to terms, selection of payment method, and order confirmation.

## Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the script using:

   ```bash
   python your_script_name.py
   ```

## Troubleshooting

- **Element Not Found**: Ensure the website structure hasn't changed, and update the XPath or CSS selectors as necessary.
- **Browser Compatibility Issues**: Verify that Chrome and ChromeDriver are up to date.
- **Pop-up Handling**: Adjust the script if any new pop-ups appear during the checkout process.

## License

This project is licensed under the MIT License.

