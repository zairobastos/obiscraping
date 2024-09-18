import pandas as pd

matriz = []

class DataQuestao:
	def __init__(self, dados:dict) -> None:
		self.dados = dados

	def questoes(self, dados:dict) -> pd.DataFrame:
		for ano, fases in dados.items():
			for fase, questoes in fases.items():
				for questao in questoes:
					link = f"https://olimpiada.ic.unicamp.br{questao['link']}"
					linha = [ano, fase, questao['nome'], link]
					matriz.append(linha)

		dataframe = pd.DataFrame(matriz, columns=['Ano', 'Fase', 'Questão', 'Link'])

		return dataframe

