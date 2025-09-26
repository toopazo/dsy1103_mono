import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("https://www.example.com")

# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Selenium" + Keys.RETURN)
# assert "Selenium" in driver.title

driver = webdriver.Chrome() # Or Firefox(), Edge(), etc.

# driver.get("https://proyectodetoxnow.github.io/ECOMERCE/login.html")
driver.get("https://vicenteavilac.github.io/index2.html")

element1 = driver.find_element(By.ID, "correo")
print(element1.text)
element1.click()
element1.send_keys("your text 1")

element2 = driver.find_element(By.ID, "password")
print(element2.text)
element2.click()
element2.send_keys("your text 2")

time.sleep(1)  # Pause to see the result

# element3 = driver.find_element(By.CLASS_NAME, "btn btn-success w-100")
element3 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print(element3.text)
element3.click()

# assert "Example Domain" in driver.title
# print("Test completed successfully.")

element1.send_keys("your text 1")


time.sleep(5)  # Pause to see the result
driver.quit()