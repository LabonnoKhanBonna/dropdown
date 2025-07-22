from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

test_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(test_url)

# We can select dropdown in 3 different way

dropdown_element = driver.find_element(By.CSS_SELECTOR,"#dropdown")
select =Select(dropdown_element)
option_count = len(select.options)

print(option_count)

expected_count = 5
if option_count == expected_count:
    print("Expected count match ")
else:
    print("Expected count mismatched ")
