from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver import ChromeOptions, Chrome

from selenium.webdriver.support.ui import Select

import pandas as pd

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import random

# Generate a random integer between 1 and 100
random_integer = random.randint(2, 8)
# print(random_integer)


options = Options()
#esta opcao serve para nao fechar o navegador apos a execucao do script
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# driver=webdriver.Chrome(service=servico, options=opts)


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ChromeOptions, Chrome

# from selenium.webdriver.support.ui import Select

# import pandas as pd

# #Chrome
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# opts = ChromeOptions()
# #esta opcao serve para nao fechar o navegador apos a execucao do script
# opts.add_experimental_option("detach", True)
# servico=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=servico, options=opts)

# driver.get("https://transparencia.ro.gov.br/pessoal")

# driver.implicitly_wait(3) # seconds


# cockie = driver.find_element(By.CLASS_NAME,'btn-consent-cookie')
# # print(cockie)
# cockie.click()

# lugar = driver.find_elements(By.CLASS_NAME,'filter-option')[4]
# # lugar1 = lugar.find_element(By.ID,'bs-select-5-1')
# driver.execute_script("arguments[0].click();",lugar)

# # .send_keys("2022" + Keys.RETURN)

# # pm = bs-select-5-24

# ano = driver.find_element(By.ID,'bs-select-5-24')
# driver.execute_script("arguments[0].click();",ano)
# # sepog = bs-select-5-39


# pag = driver.find_elements(By.CLASS_NAME,'page-link')[7]
# # driver.execute_script("arguments[0].click();", prox)
# print(pag.text)
# qtd_pag = int(pag.text)

# novolink = []

# tabela = driver.find_element(By.ID,'tabela')

# for item in tabela.find_elements(By.TAG_NAME,'a'):
#     href = item.get_attribute('href')
#     novolink.append(href)


# sleep(5)
     
# prox = driver.find_elements(By.CLASS_NAME,'page-link')[8]
# driver.execute_script("arguments[0].click();", prox)

# page = 3

contador = 0

# for item in range(qtd_pag):
#     # print('rayson')
#     sleep(5)
#     prox = driver.find_elements(By.CLASS_NAME,'page-link')[8]
#     driver.execute_script("arguments[0].click();", prox)
#     sleep(5)
#     for item in tabela.find_elements(By.TAG_NAME,'a'):
#         href = item.get_attribute('href')
#         novolink.append(href)
#     contador +=1
#     print(contador)

# print(novolink)
# print(len(novolink))

# df_links = pd.DataFrame(novolink)
# df_links.to_excel("df_links_pm.xlsx",index=False)

df_links2 = pd.read_excel('df_links_extrair_final_sepog_final.xlsx',engine='openpyxl')
print(df_links2)

qtd = df_links2[0].count()
qtd_int = int(qtd)

div = round(qtd_int/3)


print('segue o df_1')
df_1 = df_links2.loc[0:div]
print(df_1)

print('segue o df_2')
df_2 = df_links2.loc[div+1:div+div]
print(df_2)


print('segue o df_3')
df_3 = df_links2.loc[(div+div)+1:qtd_int]
print(df_3)


novoslinks1 = df_1[0].to_list()
novoslinks2 = df_2[0].to_list()
novoslinks3 = df_3[0].to_list()

dados_servidor_1 = []


for linkAtual in novoslinks1:
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

    dados_servidor_1.append((nome,cargo1,grupo1,grupo2,grupo3,grupo4))
    contador +=1
    print(contador)
    
print(dados_servidor_1)
print(len(dados_servidor_1))

df_dados_servidor_1 = pd.DataFrame(dados_servidor_1)
print(df_dados_servidor_1)
# print(df.shape)

df_dados_servidor_1.to_excel("dados_gerais_parteI.xlsx",index=False)

print("código finalizado_parteI")


dados_servidor_2 = []

for linkAtual in novoslinks2:
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

    dados_servidor_2.append((nome,cargo1,grupo1,grupo2,grupo3,grupo4))
    contador +=1
    print(contador)
    
print(dados_servidor_2)
print(len(dados_servidor_2))

df_dados_servidor_2 = pd.DataFrame(dados_servidor_2)
print(df_dados_servidor_2)
# print(df.shape)

df_dados_servidor_2.to_excel("dados_gerais_II.xlsx",index=False)

print("código finalizado_parteII")



dados_servidor_3 = []

for linkAtual in novoslinks3:
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

    dados_servidor_3.append((nome,cargo1,grupo1,grupo2,grupo3,grupo4))
    contador +=1
    print(contador)
    
print(dados_servidor_3)
print(len(dados_servidor_3))

df_dados_servidor_3 = pd.DataFrame(dados_servidor_3)
print(df_dados_servidor_3)
# print(df.shape)

df_dados_servidor_3.to_excel("dados_gerais_III.xlsx",index=False)

print("código finalizado_parteIII")


df_final_servidor = pd.concat([df_dados_servidor_1,df_dados_servidor_2,df_dados_servidor_3])
df_final_servidor.to_excel('df_completo.xlsx')
