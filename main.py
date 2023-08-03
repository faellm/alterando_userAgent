from selenium import webdriver
from time import sleep
# Definir o novo user-agent que você deseja utilizar
new_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"

# Definir as opções do navegador com o user-agent personalizado
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={new_user_agent}')

# Inicializar o navegador com as opções configuradas
driver = webdriver.Chrome(options=options)

# Fazer uma requisição para um site e verificar o user-agent
driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AXo7B7U_hveWBNXZoTw7X6i89scYFWEajobRDNT54S8iCsSV0kHDn03wkln1PqLMzD__uo8hp9l6&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S571445266%3A1691062973260323')

print("User Agent do navegador selenium:")
print(driver.execute_script("return navigator.userAgent;"))
print("________________________________________________")

sleep(20000000)

# Fechar o navegador após a execução
#driver.quit()
