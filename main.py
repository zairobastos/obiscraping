from src.codes.lista_questao import ListaQuestao
from src.codes.ajuste_lista_questao import AjusteListaQuestao
from src.codes.matriz import DataQuestao
from src.codes.prompt import Prompt
from src.codes.questao import Questao
from src.codes.gemini import Gemini

import pandas as pd
import time
import tqdm
import os

class Main:
	def __init__(self, url:str) -> None:
		self.url = "https://olimpiada.ic.unicamp.br/pratique/p2/"

	def execute(self) -> None:
		"""Método que executa as classes e métodos.

		Args:
			url (str): URL da página com as questões.

		Returns:
			None
		"""		
		lista_questao = ListaQuestao(self.url)
		dados = lista_questao.lista_de_questoes(self.url)

		ajuste_lista_questao = AjusteListaQuestao(dados)
		dados_ajustados = ajuste_lista_questao.ajuste_lista_questao(dados)

		matriz = DataQuestao(dados_ajustados)
		dataframe = matriz.questoes(dados_ajustados)

		dataframe.to_csv('questoes.csv', index=False)

		print(dataframe)

	def prompts(self, url:str) -> str:
		questao = Questao(url).texto()
		result = Prompt(questao).texto()
		return result

	def gemini_ia(self,prompt:str) -> str:
		resultado = Gemini(prompt=prompt).generate(prompt)
		return resultado

		

execute = Main("https://olimpiada.ic.unicamp.br/pratique/p2/")

dados = pd.read_csv('questoes.csv')
tqdm = tqdm.tqdm(dados['Link'])
for url in tqdm:
	prompt = execute.prompts(url)
	resultado = execute.gemini_ia(prompt)
	resultado = [item.strip('" \n').strip() for item in resultado.split(',')]
	print(resultado)
	time.sleep(3)
	os.system('cls' if os.name == 'nt' else 'clear')
