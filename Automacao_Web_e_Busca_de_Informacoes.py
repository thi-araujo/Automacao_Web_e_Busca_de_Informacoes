from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# baixar o "chromedriver.exe" e comlocar na mesma psta onte esta instalado o python
navegador = webdriver.Chrome()
# navegador = webdriver.Chrome("chromedriver.exe") # -> quando o chromedriver estiver no mesmo local
navegador.get("https://www.google.com.br/")