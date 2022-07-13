import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome version: 103

email = 'oemaillll'
senha = 'asenhaaaa'

navegador = webdriver.Chrome()

navegador.get('https://login.live.com/')            # o navegador abre esse site

preencherEmail = navegador.find_element(By.XPATH,'//*[@id="i0116"]')    # o robo procura o elemento para preencher o email
preencherEmail.send_keys(email)             # o robo preenche o email
navegador.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()       # o robo clica no botão de login

time.sleep(3)                                                           # o robo espera 3 segundos

preencherSenha = navegador.find_element(By.XPATH,'//*[@id="i0118"]')    # o robo procura o elemento para preencher a senha
preencherSenha.send_keys(senha)                                      # o robo preenche a senha
navegador.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()       # o robo clica no botão de login
