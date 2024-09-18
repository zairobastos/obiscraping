# Importando as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup


class ListaQuestao:
	def __init__(self, url:str) -> None:
		"""Classe que contém a url da página com as questões.

		Args:
			url (str): URL da página com as questões.

		Returns:
			None
		"""		
		self.url = url
		
	def lista_de_questoes(self, url:str) -> dict:
		"""Método que retorna um dicionário com as questões.

		Args:
			url (str): URL da página com as questões.

		Returns:
			dict: Dicionário com as questões.
		"""		
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		dados = {}

		anos = soup.find_all('h2')
		for ano in anos:
			ano_tag = ano.find('a')
			if ano_tag:
				ano_texto = ano_tag.get_text(strip=True)
				dados[ano_texto] = {}

				div_fases = ano.find_next_sibling('div')
				if div_fases:
					fases = div_fases.find_all('h3')
					for fase in fases:
						fase_tag = fase.find('a')
						if fase_tag:
							fase_texto = fase_tag.get_text(strip=True)
							dados[ano_texto][fase_texto] = []

							ul_questoes = fase.find_next_sibling('div')
							if ul_questoes:
								questoes = ul_questoes.find_all('li', class_='atask')
								for questao in questoes:
									link_tag = questao.find('a')
									if link_tag:
										link = link_tag['href']
										nome_questao = link_tag.get_text(strip=True)
										dados[ano_texto][fase_texto].append({'nome': nome_questao, 'link': link})

		return dados