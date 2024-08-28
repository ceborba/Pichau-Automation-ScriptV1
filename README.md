Automação de Compra de Hardware em Lives do YouTube

Este projeto é uma automação desenvolvida em Python usando Selenium para realizar compras automáticas de itens de hardware durante as transmissões ao vivo da Pichau no YouTube. Abaixo estão os principais detalhes e funcionamento da automação:

Descrição

O script automatiza o processo de compra de itens em promoção que são anunciados em tempo real no chat das lives da Pichau no YouTube. Quando um item é promovido, o programa realiza as seguintes etapas para garantir a compra rápida e eficiente:

Monitoramento de Lives: O script acessa e monitora as transmissões ao vivo da Pichau no YouTube para detectar promoções de hardware anunciadas no chat. Captura de Promoções: Assim que um item em promoção é identificado, o script extrai as informações necessárias do chat, como o link para a página do produto.

Automação de Navegação: O script abre o navegador, acessa a página do produto e executa a compra automaticamente. Compra Automática: Após adicionar o item ao carrinho, o script completa o processo de checkout com as credenciais e informações previamente configuradas.

Funcionalidades

Acesso ao YouTube: Navega até a transmissão ao vivo da Pichau no YouTube. Análise de Chat: Monitora e analisa o chat da transmissão ao vivo para identificar links enviados pela Pichau. Automação de Navegação e Compra: Abre a página do produto, adiciona-o ao carrinho e realiza a compra automaticamente. Personalização: Permite a configuração de credenciais e preferências de compra para adaptação às necessidades do usuário.

Requisitos

Python 3.11 Selenium WebDriver (ChromeDriver ou equivalente)

Como Usar

Instalação: Clone o repositório e instale as dependências necessárias. Configuração: Atualize as variáveis de configuração com suas credenciais e preferências. Execução: Execute o script e deixe-o monitorar as transmissões ao vivo para realizar a compra automaticamente.

Observações

Responsabilidade: Use o script de maneira ética e responsável, respeitando as políticas da Pichau e as normas de uso do YouTube. Manutenção: O script pode precisar de ajustes conforme mudanças na interface do YouTube ou na página de checkout da Pichau.
