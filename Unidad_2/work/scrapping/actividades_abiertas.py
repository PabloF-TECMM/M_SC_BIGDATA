from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/course/index.php")

actividades = driver.find_elements(By.CSS_SELECTOR, ".activity .instancename")
for actividad in actividades:
    print(actividad.text)

driver.quit()