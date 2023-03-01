from bs4 import BeautifulSoup
import requests
import string
#
#objeto site recebe o conteudo da requisicao.
site = requests.get("https://www.climatempo.com.br/").content

#objeto soup baixa o html do site
soup = BeautifulSoup(site, "html.parser")

#transforma o html em string e o printa o html
#print(soup.prettify())

temperatura = soup.find("h6", class_="copyright")

print(temperatura.string)

print(soup.title.string)

print(soup.a)