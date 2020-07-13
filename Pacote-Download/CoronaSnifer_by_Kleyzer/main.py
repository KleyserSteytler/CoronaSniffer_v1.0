k#from lib import Funcionabilidades
from lib import Interface
from time import sleep
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
while True:
    Interface.identifier('Corona Sniffer v1.0')
    url = 'https://www.coronatracker.com/'
    browser = webdriver.Firefox()
    browser.get(url)
    sleep(5)
    nrdeinfect = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')
    nrdeinfecttexto = nrdeinfect.text
    nrderecup = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')
    recuptexto = nrderecup.text
    nrdemortes = browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
    nrdemortestexto = nrdemortes.text
    data = date.today()
    print(f'Hoje dia {data.day} de {data.month} de {data.year} Existem:')
    print(f'{nrdeinfecttexto} no total de infectados')
    print(f'{recuptexto} no total de recuperados')
    print(f'{nrdemortestexto} no total de mortes actuais')
    sleep(5)
    print('--------------------------------------------')
    resp = input('DESEJA continuar? [S/N]: ').upper()
    if resp == 'S':    
        clear = lambda: os.system('cls')
        clear()
    else:
        break