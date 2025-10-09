from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/course/index.php")

# Selector ejemplo, puedes inspeccionar el sitio y ajustar
cursos = driver.find_elements(By.CSS_SELECTOR, ".coursename a")
for curso in cursos:
    print(curso.text)

driver.quit()