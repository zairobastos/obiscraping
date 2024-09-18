# Importando as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup

class Questao:
	def __init__(self, url:str) -> str:
		self.url = url

	def texto(self) -> str:

		response = requests.get(self.url)
		soup = BeautifulSoup(response.text, "html.parser")

		paragrafos = soup.find('div', class_='col-xl-8').find_all('p')
		texto_paragrafos = []

		for paragrafo in paragrafos:
			texto_paragrafos.append(paragrafo.get_text())

		return texto_paragrafos[1]