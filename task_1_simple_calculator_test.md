
# Test Cases for Simple Calculator Application

# Test Case 1: Addition of Two Positive Numbers
- Test Case ID: TC_ADD_01
- Test Description: Verify that the calculator correctly adds two positive numbers.
- Preconditions: The calculator application is open and ready for input.
- Test Steps:  
  1. Enter `5` in the first input field.  
  2. Enter `3` in the second input field.  
  3. Click on the `+` (Add) button.  
- Expected Result: The result displayed should be `8`.
- Actual Result: ✅ Successful, result is correct.

---

# Test Case 2: Subtraction of a Larger Number from a Smaller Number
- Test Case ID: TC_SUB_02
- Test Description: Verify that the calculator correctly subtracts when the first number is smaller.
- Preconditions: The calculator application is open.
- Test Steps:  
  1. Enter `4` in the first input field.  
  2. Enter `9` in the second input field.  
  3. Click on the `-` (Subtract) button.  
- Expected Result: The result displayed should be `-5`.
- Actual Result: ✅ Successful, result is correct.

---

# Test Case 3: Multiplication of a Positive and Negative Number
- Test Case ID: TC_MUL_03
- Test Description: Verify multiplication of a positive and a negative number.
- Preconditions: The calculator is operational.
- Test Steps:  
  1. Enter `7` in the first input field.  
  2. Enter `-2` in the second input field.  
  3. Click on the `×` (Multiply) button.  
- Expected Result: The result displayed should be `-14`.
- Actual Result: ✅ Successful, result is correct.

---

# Test Case 4: Division by Zero
- Test Case ID: TC_DIV_04
- Test Description: Verify that division by zero is handled properly.
- Preconditions: The calculator is open.
- Test Steps:  
  1. Enter `10` in the first input field.  
  2. Enter `0` in the second input field.  
  3. Click on the `÷` (Divide) button.  
- Expected Result: The calculator should display an error message such as `"Cannot divide by zero"`.
- Actual Result: ⚠️ Division by zero shows `Infinity` instead of an error message.

---

# Test Case 5: Handling Non-Numeric Inputs
- Test Case ID: TC_INV_05
- Test Description: Verify that entering non-numeric inputs results in an error.
- Preconditions: The calculator application is open.
- Test Steps:  
  1. Enter `"abc"` in the first input field.  
  2. Enter `5` in the second input field.  
  3. Click on any operation button.  
- Expected Result: The calculator should display an error message such as `"Invalid input"`.
- Actual Result: ❌ There is no option to enter non-numeric characters in the calculator.

---

# Test Case 6: Applying BODMAS Rule
- Test Case ID: TC_BODMAS_06
- Test Description: Verify that the calculator follows the correct order of operations.
- Preconditions: The calculator application supports multi-step expressions.
- Test Steps:  
  1. Enter the expression `3 + 5 / 2` in the input field.  
  2. Click on the `=` button.  
- Expected Result: The result displayed should be `5.5`, following BODMAS.
- Actual Result: ❌ The calculator evaluates it as `(3 + 5) / 2 = 4`, failing BODMAS rule.

---

# Test Case 7: Division by a Non-Zero Number
- Test Case ID: TC_DIV_07
- Test Description: Verify that the calculator correctly divides a number by a non-zero number.
- Preconditions: The calculator application is open.
- Test Steps:  
  1. Enter `0` in the first input field.  
  2. Enter `5` in the second input field.  
  3. Click on the `÷` (Divide) button.  
- Expected Result: The result displayed should be `0`.
- Actual Result: ✅ Successful, result is correct.

---

# Test Case 8: Decimal Handling
- Test Case ID: TC_DEC_08
- Test Description: Verify that the calculator correctly handles decimal calculations.
- Preconditions: The calculator supports decimal inputs.
- Test Steps:  
  1. Enter `5.5` in the first input field.  
  2. Enter `2.3` in the second input field.  
  3. Click on the `+` button.  
- Expected Result: The result displayed should be `7.8`.
- Actual Result: ✅ Successful, result is correct.

---

# Test Case 10: Maximizing the Calculator Screen
- Test Case ID: TC_MAX_10
- Test Description: Verify that the calculator works properly when the screen is maximized.
- Preconditions: The calculator application is open and running.
- Test Steps:
  1. Maximize the calculator screen.
  2. Perform any basic calculation (e.g., 5 + 3).
- Expected Result: The calculator should function properly after maximizing the screen, and the result should be displayed correctly.
- Actual Result: ❌ The calculator stops functioning properly after maximizing the screen (e.g., buttons may become unresponsive).

# Overall Application Performance
⚠️ The application is working smoothly without errors, but it fails to apply the BODMAS rule correctly in certain cases.
