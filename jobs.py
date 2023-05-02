import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace these with your own credentials and target URL
url = "https://mytime.oregonstate.edu/"
username = "XXXXXXX"  #add your username
password = "XXXXX" #add your password 

# Set up the browser and navigate to the target URL
driver = webdriver.Chrome()
driver.get(url)

# Find the username and password input fields and enter your credentials
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")
username_input.send_keys(username)
password_input.send_keys(password)

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the login to complete
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "some_element_after_login"))
)

# Find the start and stop buttons
start_button = driver.find_element_by_id("start_button_id")
stop_button = driver.find_element_by_id("stop_button_id")

# Start and stop the button at specific times
start_time = "08:00:00"  # 8 AM
stop_time = "17:00:00"   # 5 PM

while True:
    current_time = time.strftime("%H:%M:%S")
    
    if current_time == start_time:
        start_button.click()
        print("Button started at", current_time)
        time.sleep(1)
    
    if current_time == stop_time:
        stop_button.click()
        print("Button stopped at", current_time)
        time.sleep(1)
        
    time.sleep(1)

# Close the browser when done
driver.quit()
