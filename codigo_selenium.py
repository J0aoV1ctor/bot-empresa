from selenium import webdriver
import time
#abrir o navegador 
navegador = webdriver.Chrome()

#acessar um site 
navegador.get("https://www.hashtagtreinamentos.com")

#colocar o navegador em tela cheia 
navegador.maximize_window()

#selecionar um elemento na tela 
botao_verde = navegador.find_element("class name","botao-verde")

#clicar no elemento 
botao_verde.click() 

#selecionar mais de um elemento 
lista_botoes = navegador.find_elements("class name","header__titulo")
for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break
#selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

# navegar para um site diferete
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

# escrever em um campo/formulario 
navegador.find_element("id","firstname").send_keys("João Victor")
time.sleep(1)
navegador.find_element("id","email").send_keys("lalala@gmail.com ")
time.sleep(1)
navegador.find_element("id","phone").send_keys("(61)992537592")
time.sleep(1)

botao_quero_clicar = navegador.find_element("id","_form_2475_submit")

#dar scroll (colocar um elemento na tela)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_quero_clicar )

time.sleep(10)