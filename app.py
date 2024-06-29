from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import openpyxl

driver = webdriver.Chrome()

driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)

email = driver.find_element(By.XPATH, "//input[@id='email']")
sleep(2)
email.send_keys('admin@contabilidade.com')

senha = driver.find_element(By.XPATH, "//input[@id='senha']")
sleep(2)
senha.send_keys('contabilidade123456')

botao_entrar = driver.find_element(By.XPATH, "//button[@id='Entrar']")
sleep(2)
botao_entrar.click()

empresas = openpyxl.load_workbook('./empresas.xlsx')
pagina_empresas = empresas['dados empresas']

wait = WebDriverWait(driver, 10)

for linha in pagina_empresas.iter_rows(min_row=2, values_only=True):
    nome_empresa, email_empresa, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_fundacao = linha

    wait.until(EC.presence_of_element_located((By.ID, "nomeEmpresa"))).send_keys(nome_empresa)
    sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, 'emailEmpresa'))).send_keys(email_empresa)
    sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, 'telefoneEmpresa'))).send_keys(telefone)
    sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, 'enderecoEmpresa'))).send_keys(endereco)
    sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, 'cnpj'))).send_keys(cnpj)
    sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, 'areaAtuacao'))).send_keys(area_atuacao)
    sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, 'numeroFuncionarios'))).send_keys(quantidade_de_funcionarios)
    sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, 'dataFundacao'))).send_keys(data_fundacao)
    sleep(1)
    
    wait.until(EC.element_to_be_clickable((By.ID, 'Cadastrar'))).click()
    sleep(3)