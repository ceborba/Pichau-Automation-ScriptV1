from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# XPath of the buttons

password = '//*[@id="password"]'
accessAccount = '//*[@id="__next"]/div[1]/main/div[1]/div/div/div[1]/div/form/button'
urlSite = 'https://www.pichau.com.br/account'


class Checkout: 
    login = '//*[@id="username"]'

    def __init__(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-dev-tools')
        self.browser = Chrome(options=chrome_options)
        
        self.browser.get(urlSite)

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, self.login)))
        self.startLogin()
        self.main_window = self.browser.current_window_handle  
        time.sleep(5)



    def startLogin(self):
        try:
            campo_login = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.login))
            )
            self.browser.execute_script("arguments[0].scrollIntoView(true);", campo_login)

            if campo_login.is_enabled():
                campo_senha = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, password))
                )

                if campo_senha.is_enabled():
                    campo_login.send_keys(input("Digite o login: "))
                    campo_senha.send_keys(input("Digite a senha: "))

                    time.sleep(1)

                    botao_submit = WebDriverWait(self.browser, 15).until(
                        EC.element_to_be_clickable((By.XPATH, accessAccount))
                    )

                    if botao_submit.is_displayed():
                        botao_submit.click()
                        print(f'Login realizado com sucesso')
                    else:
                        print("Botão de submissão não está visível.")
                else:
                    print("Campo de senha não está habilitado.")
            else:
                print("Campo de login não está habilitado.")

        except Exception as e:
            print(f"Erro na hora do login: {e}")
