class AjusteListaQuestao:
	def __init__(self, dados:dict) -> dict:
		"""Classe que ajusta a lista de questões.

		Args:
			dados (dict): Dicionário com as questões.

		Returns:
			dict: Dicionário com as questões ajustadas.
		"""		
		self.dados = dados

	def ajuste_lista_questao(self, dados:dict) -> dict:
		"""Método que ajusta a lista de questões.

		Args:
			dados (dict): Dicionário com as questões.

		Returns:
			dict: Dicionário com as questões ajustadas.
		"""		
		novo_dicionario = {}
		for ano, fases in dados.items():
			novo_dicionario[ano] = {}

			fase3_existe = "Fase 3" in fases
			novo_dicionario[ano]["Fase 3"] = fases["Fase 3"] if fase3_existe else []

			novo_dicionario[ano]["Fase 2"] = []
			for item_f2 in fases["Fase 2"]:
				if not fase3_existe or (fase3_existe and item_f2 not in fases["Fase 3"]):
					novo_dicionario[ano]["Fase 2"].append(item_f2)

			novo_dicionario[ano]["Fase 1"] = []
			for item_f1 in fases["Fase 1"]:
				if (not fase3_existe and item_f1 not in fases["Fase 2"]) or \
					(fase3_existe and item_f1 not in fases["Fase 2"] and item_f1 not in fases["Fase 3"]):
					novo_dicionario[ano]["Fase 1"].append(item_f1)

		return novo_dicionario