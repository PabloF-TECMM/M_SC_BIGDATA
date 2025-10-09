from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/course/index.php")

categorias = driver.find_elements(By.CSS_SELECTOR, ".categoryname")
for categoria in categorias:
    print(categoria.text)

driver.quit()