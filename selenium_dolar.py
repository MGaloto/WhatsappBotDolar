from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep


#  Ejecutar URL dolarhoy

chromedriverexe = 'chromedriver.exe'
    
driver_dolar = webdriver.Chrome(chromedriverexe)
url_dolar = "https://dolarhoy.com/cotizaciondolarblue"

sleep(3)


#  Ejecutar URL ambito

driver_dolar_ambito = webdriver.Chrome(chromedriverexe)
url_dolar_ambito = "https://www.ambito.com/contenidos/dolar-informal.html"


sleep(3)


#  Ejecutar URL whatsappp

driver = webdriver.Chrome(chromedriverexe)
driver.get("https://web.whatsapp.com/")

sleep(10)

#  Enviar mensaje automatico con un while

contador = 0
while True:
    contador += 1
    driver_dolar = webdriver.Chrome(chromedriverexe)
    driver_dolar.get(url_dolar)
    sleep(2)
    html_dolar = driver_dolar.execute_script('return document.documentElement.outerHTML')
    dom = BS(html_dolar,'html.parser')
    driver_dolar.close()
    cotizaciones = dom.find_all(href="/cotizaciondolarblue")
    venta = cotizaciones[0].find(class_="venta").text
    compra = cotizaciones[0].find(class_="compra").text
    dolarhoy = "Dolarhoy.com" + " ---> " + compra + " / " + venta
    driver_dolar_ambito = webdriver.Chrome('chromedriver.exe')
    driver_dolar_ambito.get(url_dolar_ambito)
    sleep(2)
    driver_dolar_ambito.find_element_by_id("onesignal-slidedown-cancel-button").click()
    html_dolar_ambito = driver_dolar_ambito.execute_script('return document.documentElement.outerHTML')
    dom_ambito = BS(html_dolar_ambito,'html.parser')
    driver_dolar_ambito.close()
    cotizaciones_ambito = dom_ambito.find_all(class_="variacion-max-min indicador")
    venta_ambito = cotizaciones_ambito[0].find(class_="value data-venta").text.replace(',','.')
    compra_ambito = cotizaciones_ambito[0].find(class_="value data-compra").text.replace(',','.')
    ambito = "Ambito.com" + " ---> " + compra_ambito + " / " + venta_ambito
    name = "Juli"
    text = dolarhoy #+ "\n" + ambito
    print(name, ' ---> ', text)
    message = f'{text}' 
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()
    sleep(1)
    text_box = driver.find_element_by_class_name("p3_M1")
    sleep(1)
    text_box.send_keys(message)
    sleep(1)
    clickear = driver.find_element_by_class_name("_4sWnG")
    sleep(1)
    clickear.click()
    sleep(1)
    print('Mensaje N° ' + str(contador) + ' enviado.')
    
    
    
    
    
    
    
    