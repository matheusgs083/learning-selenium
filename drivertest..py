from time import sleep
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyautogui import press

# === Configurações ===

DRIVER_PATH = r"C:\\Users\\caixa.patos\\Documents\\IEDriverServer.exe"
URL = "http://paubrasil.promaxcloud.com.br/pw/"
USUARIO = "F7367"
SENHA = "Matheus2"
TIMEOUT = 10

# === Inicia o driver do Internet Explorer ===

service = Service(executable_path=DRIVER_PATH)
options = webdriver.IeOptions()
options.ignore_protected_mode_settings = True

driver = webdriver.Ie(service=service, options=options)
wait = WebDriverWait(driver, TIMEOUT)

# === Acessa o sistema ===

driver.get(URL)
driver.switch_to.frame("top")
print("Página atual:", driver.current_url)

# Login

login = wait.until(EC.presence_of_element_located((By.NAME, "Usuario")))
senha = wait.until(EC.presence_of_element_located((By.NAME, "Senha")))
login_btn = wait.until(EC.presence_of_element_located((By.NAME, "cmdConfirma")))

login.send_keys(USUARIO)
senha.send_keys(SENHA)

login_btn.click()

# ESCOLHER REVENDA

...

# # Confirma novamente após login
confirm_btn = wait.until(EC.presence_of_element_located((By.NAME, "cmdConfirma")))
confirm_btn.click()

# Trata alertas pós-login
for i in range(5):
    sleep(0.5)
    press("enter")

# Aguarda antes de encerrar
sleep(5)
driver.quit()
