# Biblioteca requests - usada para fazer requisições HTTP, simplificando o processo de envio de solicitações (GET, POST, PUT, DELETE) para servidores web.
import requests
# Biblioteca BeautifulSoup - usada para extrair e manipular dados de documentos HTML/XML.
from bs4 import BeautifulSoup

# Define a funçao "extrair_urls" com o parâmetro "url".
def extrair_urls(url):
    # Adiciona um User-Agent ao cabeçalho para simular uma solicitação feita por um navegador, evitando assim, um erro 403 (Forbidden).
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Tenta fazer a solicitação HTTP com timeout.
    # Este bloco de código trata eventuais erros que podem acontecer durante a execução da solicitação HTTP usando a biblioteca requests.
    try:
        resposta = requests.get(url, headers=headers, timeout=5)
        resposta.raise_for_status()  # Lança uma exceção para códigos de status HTTP diferentes de 2xx.
    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de Conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout de Solicitação:", errt)
    except requests.exceptions.RequestException as err:
        print("Erro na Solicitação:", err)
        return []  # Retorna uma lista vazia em caso de erro.
    
    # Faz a solicitação HTTP para obter o conteúdo da página.
    # resposta = requests.get(url, headers=headers)
    
    # Define a lista para armazenar as URLs.
    urls = []
    
    # Verifica se a solicitação foi bem-sucedida (código de status 200).
    if resposta.status_code == 200:
        # Analisa o HTML da página usando BeautifulSoup.
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        # Encontra todos os elementos 'a' (links) na página.
        links = soup.find_all('a')
        
        # Extrai as URLs e adiciona à lista.
        for link in links:
            href = link.get('href')
            if href:
                urls.append(href)

    else:
        print(f"Erro ao acessar a página. Código de status: {resposta.status_code}")
    
    # Retorna a lista de URLs.
    return urls

# Substitua a URL abaixo pela página que você deseja fazer scraping.
url_alvo = "https://algumaurl.com.br/"

# Chama a função para extrair as URLs.
urls_capturadas = extrair_urls(url_alvo)

# Exibe as URLs capturadas.
for url in urls_capturadas:
    print(url)
