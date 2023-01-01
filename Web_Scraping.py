from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content

#objeto site recebendo o conteudo da requisição http
soup = BeautifulSoup(site, 'html.parser')

#objeto soup está baixando o html do site
print(soup.prettify())

#pode filtrar
temperatura = soup.find("span", class_ = "teste")

print(temperatura)

# pode pegar informações pelas tags
print(soup.title.string)