from selenium import webdriver
import time 
# abrir o navegador
navegador = webdriver.Chrome ()
#acessar o site
navegador.get("https://7lm.cvcrm.com.br/gestor/")
#colocar o navegador em tela cheia
navegador.maximize_window()
#selecionar um elemento na tela 
seu_email=navegador.find_element("class name","form-control")
#clicar no elemento
seu_email.click()
# encontrar varios elementos dentro da pagina

campos=navegador.find_elements("class name","form-control")

for senha in campos:
    if senha in campos.text:
        seu_email.click()

time.sleep(10)