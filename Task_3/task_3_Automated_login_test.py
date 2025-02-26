from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Open the web application
driver.get("https://www.saucedemo.com/")

# Valid usernames with different passwords
valid_users = {
    "standard_user": "secret_sauce",
    "locked_out_user": "secret_sauce",
    "problem_user": "secret_sauce",
    "performance_glitch_user": "sauce_secret",  # Modified password for testing
    "error_user": "secretsauce",  # Modified password for testing
    "visual_user": "1234_sauce"  # Modified password for testing
}

# Invalid usernames
invalid_users = {
    "unknown_user1": "random_password",
    "fake_user": "fake_pass123",
    "test123": "wrongpassword",
    "invalid_login": "not_a_real_pass"
}

# Test Case 1: Valid Logins
def test_valid_logins():
    for username, password in valid_users.items():
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        if "inventory.html" in driver.current_url:
            print(f"✅ Login successful for: {username} with password: {password}")
        else:
            print(f"❌ Login failed for: {username} with password: {password} (Possible incorrect password)")

        driver.get("https://www.saucedemo.com/")  # Reload page for the next test

# Test Case 2: Invalid Logins
def test_invalid_logins():
    for username, password in invalid_users.items():
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Epic sadface" in error_message  # Expected error message presence
        print(f"❌ Login failed as expected for: {username} with password: {password}")

# Test Case 3: Empty Fields
def test_empty_fields():
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_message  # Expected empty field error message
    print("⚠️ Empty fields test passed: Login failed as expected.")

# Run Tests
test_valid_logins()
test_invalid_logins()
test_empty_fields()

# Close the browser
driver.quit()
