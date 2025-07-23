from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://jqueryui.com/"
driver = webdriver.Firefox()
driver.get(url)

all_links = driver.find_elements(By.TAG_NAME,"a")
print (f"Number of Links are {len(all_links)}")
driver.quit()