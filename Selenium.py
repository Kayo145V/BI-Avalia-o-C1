from selenium import webdriver
import time
import schedule
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def download_csv():
    #Iniciando o driver do Google Chrome
    driver = webdriver.Chrome()

    #Abrindo o site
    driver.get("https://coronavirus.es.gov.br/painel-covid-19-es")

    #Esperando a página carregar
    time.sleep(10)

    #Encontrando o botão de download e clicando nele
    download_button = driver.find_element_by_css_selector(layout-wrapper > div.zone-content-wrap > div > article > div > div > div > div > div > div:nth-child(1) > p > a:nth-child(1))
    download_button.click()

    #Esperando o download ser concluído
    time.sleep(10)

    #Fechando o driver do Chrome
    driver.quit()

#Executando o download_csv() uma vez por dia, às 12h
schedule.every().day.at("12:00").do(download_csv)

while True:
    schedule.run_pending()
    time.sleep(1)