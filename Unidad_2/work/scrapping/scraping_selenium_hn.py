# Importamos las librerías necesarias para Selenium y manejo de esperas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuramos opciones de Chrome, aquí se abre maximizado
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

# Inicializamos el driver de Chrome con las opciones configuradas
driver = webdriver.Chrome(options=options)

# Abrimos la página de Hacker News
driver.get("https://news.ycombinator.com/")

# Esperamos hasta que los títulos de las noticias estén presentes en la página (máximo 10 segundos)
wait = WebDriverWait(driver, 10)
titulos = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, 'span.titleline > a')
    )
)

# Imprimimos los textos (titulos) de cada elemento encontrado
print("Títulos encontrados:")
for titulo in titulos:
    print(titulo.text)

# Cerramos el navegador y liberamos recursos
driver.quit()