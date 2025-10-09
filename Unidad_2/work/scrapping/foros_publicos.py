from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://enlinea.tecmm.mx/moodle/mod/forum/index.php") # puede requerir ajustar ruta

# Selector ejemplo
foros = driver.find_elements(By.CSS_SELECTOR, ".forumname a")
for foro in foros:
    print(foro.text)

driver.quit()