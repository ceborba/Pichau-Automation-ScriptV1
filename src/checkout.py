from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

added_product = '//*[@id="__next"]/div[1]/main/div[2]/div/div[2]/div[4]/div[2]/div[1]/button'
completedOrder = '//*[@id="__next"]/div/main/div[2]/div/div[1]/div/a'
password = '//*[@id="password"]'
accessAccount = '//*[@id="__next"]/div[1]/main/div[1]/div/div/div[1]/div/form/button'
methodPix = '//*[@id="payment-method-mercadopago_custom_pix"]/label' 
address = '//*[@id="__next"]/main/div[3]/div/div/div/div[1]/div[2]/div/div[1]/label/span[1]'
shipping_method = '//*[@id="__next"]/div[1]/main/div[3]/div/div/div/div[1]/div[4]/div[2]/div/button'
continueReview = '//*[@id="__next"]/div/main/div[3]/div/div/div/div[1]/div[3]/div[2]/div/button'
checkbox = '//*[@id="__next"]/div[1]/main/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div/label/span[1]'
finishOrder = '//*[@id="__next"]/div[1]/main/div[3]/div/div/div/div[2]/div[2]/div[2]/button'
urlSite = 'https://www.pichau.com.br/account'
remove= '//*[@id="__next"]/div[1]/main/div[2]/div/div[2]/div[1]/table/tbody/tr/td[4]/button'

class Checkout:
 
    login = '//*[@id="username"]'

    def __init__(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        # chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-dev-tools')

        self.browser = Chrome(options=chrome_options)
        
        self.browser.get(urlSite)

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, self.login)))
        self.startLogin()
        self.main_window = self.browser.current_window_handle  
        time.sleep(4)
        self.addProductAleatory()
        self.inCart()
        # self.selectAddress()
        self.shippingMethod()
        self.main_window2 = self.browser.current_window_handle
        self.removedCart()


    def start(self, url, callback):

        self.addProduct(url)
        time.sleep(0.9)
        self.methodPayment()
        time.sleep(0.1)
        self.checkoutReview()
        self.checkbox()
        self.finish()
        time.sleep(0.5)
        callback()

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

    def addProductAleatory(self):
        try:
            main_window = self.browser.current_window_handle
            self.browser.execute_script("window.open();")
            print("Aberto nova aba para ir no produto aleatorio")
            
            new_tab = [tab for tab in self.browser.window_handles if tab != main_window][0]
            self.browser.switch_to.window(new_tab)

            self.browser.get('https://www.pichau.com.br/microfone-pichau-izar-pro-pft-rgb-usb-preto-pg-izrpft-rgb01')
            
            element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, added_product))
            )

            if element.is_displayed():
                element.click()
                print("Botão de adicionar clicado...")
            else:
                print("Elemento não está visível.")

        except Exception as i:
            print(f"Erro de carregamento: {i}")


    def inCart(self):
        try:
            print("Página carregada com sucesso")

            element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, completedOrder))
            )
            print("Adicionado ao carrinho")

            if element.is_displayed():
                element.click()
                print("Botão de finalizar pedido clicado...")
            else:
                print("Elemento não está visível.")
        except Exception as e:
                print(f"Erro de carregamento: {e}")


    # SOMENTE NECESSARIO SE O ENDEREÇO NÃO FOR SELECIONADO AUTOMATICAMENTE
    # def selectAddress(self):
    #     try:
    #         botao_submit = WebDriverWait(self.browser, 2).until(
    #             EC.element_to_be_clickable((By.XPATH, address))
    #         )
    #         if botao_submit.is_displayed():
    #             botao_submit.click()
    #             print(f"Selecionado endereço de entrega")
    #         else:
    #             print("Endereço de entrega já selecionado")

    #     except Exception as e:
    #         print(f"Erro ao clicar no botão do pagamento1: {e}") 

    def shippingMethod(self):
        try:
            WebDriverWait(self.browser, 3).until(
                EC.invisibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div/div/div/div[1]/div[2]/div/div[1]/label/span[1]/span[1]/input'))
            )
            main_window2 = self.browser.current_window_handle
            botao_submit = WebDriverWait(self.browser, 2).until(
                EC.element_to_be_clickable((By.XPATH, shipping_method))
            )
            botao_submit.click()
            print(f"Selecionado método de envio e clicado no botão de continuar pagamento")

            self.browser.switch_to.window(self.main_window)

        except Exception as e:
            print(f"Erro ao clicar no botão do pagamento2: {e}")
    
    def removedCart(self):
        try:
            self.browser.get('https://www.pichau.com.br/cart')

            element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, remove))
            )

            if element.is_displayed():
                element.click()
                print("Botão de remover clicado...")
            else:
                print("Elemento não está visível.")

        except Exception as i:
            print(f"Erro de carregamento: {i}")


    def addProduct(self, product_url):
        try:
            main_window = self.browser.current_window_handle

            self.browser.get(product_url)

            element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, added_product))
            )

            if element.is_displayed():
                element.click()
                print("Botão de adicionar ao carrinho clicado...")
            else:
                print("Elemento não está visível.")

            WebDriverWait(self.browser, 10).until(
                EC.number_of_windows_to_be(2)
            )

            # Lista todas as abas e muda para a segunda aba
            for window_handle in self.browser.window_handles:
                if window_handle != main_window:
                    self.browser.switch_to.window(window_handle)
                    break

        except Exception as i:
            print(f"Erro de carregamento: {i}")

    def methodPayment(self):
        try:
            botao_submit = WebDriverWait(self.browser, 15).until(
                EC.element_to_be_clickable((By.XPATH, methodPix))
            )
            botao_submit.click()
            print("Botão para selecionar a forma de pagamento: Pix clicado...")

        except Exception as e:
            print(f"Erro ao selecionar o metodo de pagamento: {e}")

    def checkoutReview(self):
        try:
            botao_submit = WebDriverWait(self.browser, 15).until(
                EC.element_to_be_clickable((By.XPATH, continueReview))
            )
            botao_submit.click()
            print("Clicado em continuar para a revisão")

        except Exception as e:
            print(f"Erro ao clicar no botão: {e}")

    def checkbox(self):
        try:
            print("Página do checkout carregada com sucesso...")
            botao_submit = WebDriverWait(self.browser, 15).until(
                EC.element_to_be_clickable((By.XPATH, checkbox))
            )
            botao_submit.click()
            print("Clicado em estou ciente e CONCORDO com os termos da Pichau...")

        except Exception as e:
            print(f"Erro ao clicar no botão: {e}")

    def finish(self):        
        try:
            print("Você está na ultima parte antes do pagamento, caso queira REALMENTE adquirir o produto, basta fazer o RECAPTCHA de Imagens")
            print("Caso não tenha interesse no produto, basta reiniciar o software :)")
            botao_submit = WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((By.XPATH, finishOrder))
            )
            botao_submit.click()
            print("Produto comprado com sucesso")
            print("Reinicie o software para comprar novos produtos :)")
        except Exception as e:
            print(f"Erro ao clicar no botão: {e}")

        time.sleep(2)
        self.browser.close()
        print(f"Chrome fechado!")