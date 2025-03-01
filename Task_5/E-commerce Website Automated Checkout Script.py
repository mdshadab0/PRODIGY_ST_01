from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Setup the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

# Step 1: Go to Dresses section
dresses_section = driver.find_element(By.LINK_TEXT, "DRESSES")
dresses_section.click()

# Step 2: Apply the "In Stock" filter
time.sleep(3)
instock_filter = driver.find_element(By.ID, "layered_quantity_1")
instock_filter.click()

# Step 3: Wait until the first product name is visible, then click it
wait = WebDriverWait(driver, 10)
first_product_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='product-name']")))
first_product_name.click()

# Step 4: Try different color and size combinations, attempt to add to cart, and check for the "Proceed to checkout" popup
colors = driver.find_elements(By.CSS_SELECTOR, "#color_to_pick_list li a")

proceed_to_checkout_popup = False

# Iterate through each color and size
for color_element in colors:
    color_element.click()
    time.sleep(1)

    # Step 5: Explicitly click on the size dropdown box
    size_dropdown_box = driver.find_element(By.ID, "group_1")
    size_dropdown_box.click()  # Open the dropdown

    # Step 6: Use Select to iterate over sizes S, M, and L
    sizes_dropdown = Select(driver.find_element(By.ID, "group_1"))

    # Define the sizes to try: "S", "M", "L"
    sizes_to_try = ["M", "L"]

    # Step 7: Iterate through the defined sizes
    for size_value in sizes_to_try:
        sizes_dropdown.select_by_visible_text(size_value)  # Select size from dropdown
        time.sleep(1)

        # Step 8: Try adding to cart after each combination
        add_to_cart = wait.until(EC.element_to_be_clickable((By.NAME, "Submit")))
        add_to_cart.click()

        # Step 9: Check if the "Proceed to checkout" pop-up appears
        try:
            proceed_to_checkout = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Proceed to checkout']")))
            proceed_to_checkout.click()
            proceed_to_checkout_popup = True  # Set the flag to true if the checkout popup appeared
            break
        except:
            # If the pop-up didn't appear, close any alert or continue trying next combination
            time.sleep(2)
            close_popup_button = driver.find_elements(By.CLASS_NAME, "cross")  # Close any pop-up if available
            if close_popup_button:
                close_popup_button[0].click()

    if proceed_to_checkout_popup:  # If we've successfully added to cart and clicked checkout, stop further checks
        break

# Step 10: Complete the checkout process (Proceed to summary checkout)
summary_checkout = driver.find_element(By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium']")
summary_checkout.click()

time.sleep(2)
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("mdshadab0500@gmail.com")  # Replace with your email
password_field = driver.find_element(By.ID, "passwd")
password_field.send_keys("Shadab@123")  # Replace with your password

login_button = driver.find_element(By.ID, "SubmitLogin")
login_button.click()

# Step 11: Confirm address and proceed
address_checkout = driver.find_element(By.NAME, "processAddress")
address_checkout.click()

# Step 12: Agree to the terms of service and proceed
terms_of_service = driver.find_element(By.ID, "cgv")
terms_of_service.click()

shipping_checkout = driver.find_element(By.NAME, "processCarrier")
shipping_checkout.click()

# Step 13: Choose payment method (e.g., Pay by bank wire) and confirm
pay_by_bank_wire = driver.find_element(By.CLASS_NAME, "bankwire")
pay_by_bank_wire.click()

# Step 14: Confirm the order
confirm_order_button = driver.find_element(By.XPATH, "//button[@class='button btn btn-default button-medium']")
confirm_order_button.click()

# Close the browser after completing the process
time.sleep(3)
driver.quit()