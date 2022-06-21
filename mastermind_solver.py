import pickle
import itertools
import collections
from create_all_plays import resultado_do_palpite


class MastermindCodeBreaker:
    def __init__(self, senha_cm):
        # Cria a lista de resultados LR
        self.lista_de_resultados = itertools.product(["R", "G", "B", "Y", "P", "O"], repeat=4)
        # A LR é uma lista de arrays, aqui o JOIN transforma em string
        self.lista_de_resultados = {"".join(answer) for answer in self.lista_de_resultados}
        # Quantidade padrão para o jogo Mastermind, mesmo sabendo que não será necessário toda essa quantidade
        self.palpites_restantes = 10
        self.historico_palpites = []
        self.historico_de_dicas = []
        self.senha_cm = senha_cm

        FileStore = open("storage/dicionario_resultados.pickle", "rb")
        self.dicionaria_de_resultados = pickle.load(FileStore)
        FileStore.close()

    def criar_palpite(self):
        palpites_para_tentativas = []
        for palpite, scores_by_answer_dict in self.dicionaria_de_resultados.items():
            # Filtra para incluir apenas as respostas possíveis
            scores_by_answer_dict = {answer: score for answer, score in scores_by_answer_dict.items()
                                     if answer in self.lista_de_resultados}
            self.dicionaria_de_resultados[palpite] = scores_by_answer_dict

            # Faz a contagem de cada um dos valores obtidos, Ex: {"BBB": 10, "B": 7, "BW": 20}
            possibilities_per_score = collections.Counter(scores_by_answer_dict.values())
            # Procura pelo pior caso, procurando qual o valor que mais se repete, no caso do Ex anterior será 20
            pior_caso = max(possibilities_per_score.values())

            # É preferível palpites possíveis em vez dos impossíveis
            palpite_impossivel = palpite not in self.lista_de_resultados
            palpites_para_tentativas.append((pior_caso, palpite_impossivel, palpite))

        # Quem vai determinar qual o próximo palpite é o minimo, temos um array de array
        # Ex: [(72, True, 'RRRR'), (64, True, 'RRRG'), (42, True, 'RRRB'),...]
        # Se o primeiro valor for igual, o segundo é quem vai desempatar,
        # nesse caso a função dá prioridade para o FALSE, ou seja, para valores possíveis.
        # Mas terão momentos em que serão utilizados palpites impossíveis.
        test = min(palpites_para_tentativas)
        test2 = test[-1]
        return test2

    def solve(self):
        while self.palpites_restantes > 0:
            if self.palpites_restantes == 10:
                palpite = "RRGG"
            else:
                palpite = self.criar_palpite()

            self.historico_palpites.append(palpite)

            resultado = resultado_do_palpite(palpite, self.senha_cm)
            self.historico_de_dicas.append(resultado)
            # Filtro em busca apenas dentro da chave do palpite pelos valores iguais ao resultado
            self.lista_de_resultados = {answer for answer in self.lista_de_resultados
                                if self.dicionaria_de_resultados[palpite][answer] == resultado}

            self.palpites_restantes -= 1
            if palpite == self.senha_cm:
                return self.historico_palpites, self.historico_de_dicas