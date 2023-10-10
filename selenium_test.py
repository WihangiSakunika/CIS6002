from selenium import webdriver
import time

# Create a WebDriver instance
driver = webdriver.Chrome()

# Open your Streamlit app
driver.get('http://localhost:8501')  # Change the URL to your app's URL

# Simulate user interactions
age_input = driver.find_element_by_id('age_input')  # Replace with the actual element ID
age_input.send_keys('30')  # Input a value for age

bmi_input = driver.find_element_by_id('bmi_input')  # Replace with the actual element ID
bmi_input.send_keys('25')  # Input a value for BMI

# You can continue to interact with other input fields and buttons as needed

# Simulate submitting the form
submit_button = driver.find_element_by_id('submit_button')  # Replace with the actual element ID
submit_button.click()

# Wait for the results to appear
time.sleep(2)  # Adjust the sleep time as needed

# Verify the results
prediction_result = driver.find_element_by_id('prediction_result')  # Replace with the actual element ID
print("Prediction Result:", prediction_result.text)

# Close the browser window
driver.quit()
