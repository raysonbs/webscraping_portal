from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

from selenium.webdriver.support.ui import Select

import pandas as pd

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


opts = ChromeOptions()
#esta opcao serve para nao fechar o navegador apos a execucao do script
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

driver.get("https://transparencia.ro.gov.br/pessoal")

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.pinterest.com/ideas/")


driver.implicitly_wait(3) # seconds


cockie = driver.find_element(By.CLASS_NAME,'btn-consent-cookie')
# print(cockie)
cockie.click()

lugar = driver.find_elements(By.CLASS_NAME,'filter-option')[4]
# lugar1 = lugar.find_element(By.ID,'bs-select-5-1')
driver.execute_script("arguments[0].click();",lugar)

print("lugar")

# .send_keys("2022" + Keys.RETURN)

# pm = bs-select-5-24

ano = driver.find_element(By.ID,'bs-select-5-40')
driver.execute_script("arguments[0].click();",ano)
# sepog = bs-select-5-39


pag = driver.find_elements(By.CLASS_NAME,'page-link')[7]
# driver.execute_script("arguments[0].click();", prox)
print(pag.text)
qtd_pag = int(pag.text)

novolink = []

tabela = driver.find_element(By.ID,'tabela')

for item in tabela.find_elements(By.TAG_NAME,'a'):
    href = item.get_attribute('href')
    novolink.append(href)


sleep(5)
     
prox = driver.find_elements(By.CLASS_NAME,'page-link')[8]
driver.execute_script("arguments[0].click();", prox)

page = 3

contador = 0

for item in range(qtd_pag):
    sleep(5)
    prox = driver.find_elements(By.CLASS_NAME,'page-link')[8]
    driver.execute_script("arguments[0].click();", prox)
    sleep(5)
    for item in tabela.find_elements(By.TAG_NAME,'a'):
        href = item.get_attribute('href')
        novolink.append(href)
    contador +=1
    print(contador)

print(novolink)
print(len(novolink))

df_links = pd.DataFrame(novolink)
df_links.to_excel("df_links_extrair_final.xlsx",index=False)

df_links2 = pd.read_excel('df_links_extrair_final',engine='openpyxl')
print(df_links2)
novoslinks = df_links2[0].to_list()

dados_servidor = []


for linkAtual in novoslinks:
    driver.get(linkAtual)
    nome = driver.find_element(By.CLASS_NAME,'remunerecao-title-nome').text
    print('Nome:',nome)

    cargo1 = driver.find_element(By.ID,'server-salaries-40864393-tab').text
    print('Cargo1:',cargo1)
    
    grupo1 = driver.find_elements(By.CLASS_NAME,'card-block')[0].text
    grupo2 = driver.find_elements(By.CLASS_NAME,'card-block')[1].text
    grupo3 = driver.find_elements(By.CLASS_NAME,'card-block')[2].text
    grupo4 = driver.find_elements(By.CLASS_NAME,'card-block')[3].text

    print(grupo1)
    print('-------------//----------')
    print('-------------//----------')
    print(grupo2)
    print('-------------//----------')
    print('-------------//----------')
    print(grupo3)
    print('-------------//----------')
    print('-------------//----------')
    print(grupo4)
    print('-------------//----------')
    print('-------------//----------')

    dados_servidor.append((nome,cargo1,grupo1,grupo2,grupo3,grupo4))
    contador +=1
    print(contador)
    
print(dados_servidor)
print(len(dados_servidor))

df = pd.DataFrame(dados_servidor)
print(df)
# print(df.shape)

df.to_excel("df_links_extrair.xlsx",index=False)

print("código finalizado")
