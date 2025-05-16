from selenium import webdriver
import time 
# abrir o navegador
navegador = webdriver.Chrome ()
#acessar o site
navegador.get("https://7lm.cvcrm.com.br/gestor/")
#colocar o navegador em tela cheia
navegador.maximize_window()
#selecionar o elemento na tela
seu_email = navegador.find_element ("class name", "cv-btn-block -primario -big -full m-t-10 --btn-acessar")
# clicar no elemento 
seu_email.click()

time.sleep(10)
