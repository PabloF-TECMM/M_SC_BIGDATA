from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/course/index.php")

# Selector ejemplo para archivos públicos
documentos = driver.find_elements(By.CSS_SELECTOR, ".activity.resource .instancename a")
for doc in documentos:
    print(doc.text)

driver.quit()