import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

test_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(test_url)

# Find the dropdown and initialize the Select object
dropdown_element = driver.find_element(By.CSS_SELECTOR, "#dropdown")
select = Select(dropdown_element)

# Get the number of options in the dropdown
option_count = len(select.options)
print(option_count)

expected_count = 3  # There are 3 options on the page
if option_count == expected_count:
    print("Expected count match")
else:
    print("Expected count mismatched")

# Select by visible text
select.select_by_visible_text("Option 1")
time.sleep(2)

# Refresh the page — dropdown element becomes stale!
driver.refresh()
time.sleep(2)

# Re-locate the dropdown after the page refresh
dropdown_element = driver.find_element(By.CSS_SELECTOR, "#dropdown")
select = Select(dropdown_element)

# Select by index number (index starts from 0, so 2 corresponds to "Option 2")
select.select_by_index(2)

time.sleep(2)
driver.quit()
