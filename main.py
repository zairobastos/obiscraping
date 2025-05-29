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
    def __init__(self, url: str) -> None:
        self.url = url

    def execute(self) -> None:
        """Executa o pipeline para coletar e salvar questões."""
        lista_questao = ListaQuestao(self.url)
        dados = lista_questao.lista_de_questoes(self.url)

        ajuste_lista_questao = AjusteListaQuestao(dados)
        dados_ajustados = ajuste_lista_questao.ajuste_lista_questao(dados)

        matriz = DataQuestao(dados_ajustados)
        dataframe = matriz.questoes(dados_ajustados)

        dataframe.to_csv('questoes.csv', index=False)
        print("Dados coletados e salvos em 'questoes.csv'")
        print(dataframe)

    def prompts(self, url: str) -> str:
        """Gera o prompt da questão."""
        questao = Questao(url).texto()
        result = Prompt(questao).texto()
        return result

    def gemini_ia(self, prompt: str) -> str:
        """Gera o resultado usando o modelo Gemini."""
        resultado = Gemini(prompt=prompt).generate(prompt)
        return resultado


if __name__ == "__main__":
    execute = Main("https://olimpiada.ic.unicamp.br/pratique/p2/")

    # Carregar os dados salvos em 'questoes.csv'
    dados = pd.read_csv('questoes.csv')

    # Iterar sobre as primeiras 5 URLs
    data = []
    for url in tqdm.tqdm(dados['Link'][:20], desc="Processando questões"):
        prompt = execute.prompts(url)
        resultado = execute.gemini_ia(prompt)
        resultado = [item.strip('" \n').strip()
                     for item in resultado.split(',')]
        data.append([url] + resultado)
        print(f"Resultado para {url}:", resultado)

        # Pausa para evitar sobrecarga
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    # Criar o DataFrame com os resultados
    dataframe = pd.DataFrame(data, columns=[
        'URL', 'Dificuldade', 'Assunto', 'Subassunto', 'Tópico', 'Prova'
    ])
    dataframe.to_csv('resultado.csv', index=False)
    print("Resultados salvos em 'resultado.csv'")
