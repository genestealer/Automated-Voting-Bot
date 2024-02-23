from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from datetime import datetime

url = 'https://demo.com'
XPATH_X_BUTTON = "/html/body/div[2]/main/div/div/div[3]/div[2]/div[2]/div[2]/div[1]/div"
XPATH_X_TWITTER_BUTTON = "/html/body/div[2]/main/div/div/div[3]/div[2]/div[2]/div[3]/span/a/div"

# Function to check if it's daytime (6 AM to 10 PM)
def is_daytime():
    now = datetime.now()
    return 8 <= now.hour < 23

# Start browser
print("Opening Browser")
browser = webdriver.Firefox()
browser.get(url)
time.sleep(1)


# Find vote button
next_button = browser.find_element("xpath", XPATH_X_BUTTON)
time.sleep(1)

# Click vote button
print("Trying to click the button to vote.")
next_button.click()
print("Button clicked.")


# Wait for vote to be counted
sleep_duration = random.uniform(4, 8)
time.sleep(sleep_duration)

# Find newly exsposed share to twitter / X button
double_button = browser.find_element("xpath", XPATH_X_TWITTER_BUTTON)
print("Trying to click the twitter button to vote.")
double_button.click()
print("Twitter Button clicked.")
time.sleep(2)


if is_daytime():
    print("It's daytime. Now sleep for random: between 1 and 10 seconds.")
    # Generate a random sleep duration between 1 and 10 seconds during the day
    sleep_duration = random.uniform(1, 5)
else:
    print("It's nighttime. Now sleep for random: between 10 and 120 seconds.")
    # Generate a random sleep duration between 10 and 120 seconds at night
    sleep_duration = random.uniform(10, 120)

# Sleep for the generated duration
time.sleep(sleep_duration)


# Close Browser.
#close() will not delete temporary files
print("Closing Browser")
browser.quit();


exit()