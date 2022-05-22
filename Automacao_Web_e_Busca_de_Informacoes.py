# Automação Web e Busca de Informações com Python

# !pip install selenium -> Quando for usar no Jupyter Notebook instalar selenium com esse comando

# pip install selenium -> Quando usar  em uma IDE com Python instalar selenium atraves desse comando pelo terminal

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Baixar o "chromedriver.exe" e colocar na mesma pasta onde esta instalado o python
# Abrir um navegador( nesse caso Chrome)
navegador = webdriver.Chrome("chromedriver.exe")
# navegador = webdriver.Chrome("chromedriver.exe") # -> Quando o chromedriver estiver no mesmo local
navegador.get("https://www.google.com.br/")


# Passo 1: Pegar a cotação do Dólar
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Dólar")

navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_dolar)

# Passo 2: Pegar a cotação do Euro
navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Euro")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# Fechar o navegador
navegador.quit()

# Passo 4: Importar pandas para ler a base de dados

# Importar lista de produtos(base de dados)
tabela = pd.read_excel("Produtos.xlsx")
display(tabela)




# Nas linhas onde na coluna "Moeda" = Dólar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)

# Atualizar o preço base reais (preço base original * cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# Atualizar o preço final (preço base reais * Margem)
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)

display(tabela)


