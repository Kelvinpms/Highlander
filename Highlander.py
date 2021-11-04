import csv
import os
import time
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
t = time.strftime("%Y-%m-%d")
driver = webdriver.Chrome(executable_path=r"C:\Users\Kelvin\Desktop\Lista WhatsApp Python\chromedriver.exe")
site = 'https://web.whatsapp.com/'
driver.get(site)
lista_resultados = []
input("Pressione qualquer coisa após QR scan")
nomesdosgrupos = ["Highlander"]
for name in nomesdosgrupos:
    person = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
    person.click()
for contatos in driver.find_elements_by_css_selector("._1B9Rc span:nth-child(1)"): 
    time.sleep(3)
    lista_resultados.append(contatos)
    line = contatos.text 
    print(line)
Lupa = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[1]')
Clica_Fora_da_Lupa = Lupa
Acao_Fora_da_Lupa = webdriver.common.action_chains.ActionChains(driver)
Acao_Fora_da_Lupa.move_to_element_with_offset(Clica_Fora_da_Lupa,0,100)
Acao_Fora_da_Lupa.click()
Acao_Fora_da_Lupa.perform()
Acao_Fora_da_Lupa.click()
Acao_Fora_da_Lupa.perform()
with open('resultado_da_participacao'  +t+  '.txt',"w") as arquivo:
    arquivo.write('resultado_da_participacao'+'\n')
    while len(driver.find_elements_by_class_name("_3DF-v") ) == 0:
        time.sleep(2)
        for contatos in driver.find_elements_by_css_selector("._1B9Rc span:nth-child(1)"): 
            lista_resultados.append(contatos)
            line = contatos.text 
            print(line)
            html = driver.find_element_by_tag_name('html')
            html.send_keys(Keys.PAGE_UP)
            arquivo.write(line+'\n')
    arquivo.close() 
    wb = openpyxl.Workbook()
    ws = wb.worksheets[0]        
input_file = 'resultado_da_participacao'  +t+  '.txt'
output_file = r'resultado_da_participacao'  +t+  '.xlsx' 
with open(input_file, 'r') as data:
    reader = csv.reader(data, delimiter='\t')
    for row in reader:
        ws.append(row)
wb.save(output_file)
dataframe = pd.read_excel('resultado_da_participacao'  +t+  '.xlsx')
dataframe['resultado_da_participacao'].value_counts() 