import pickle
import itertools
import collections
from create_all_plays import score_guess


class MastermindCodeBreaker:
    def __init__(self, answer):
        # Cria a lista de resultados LR
        self.all_answers = itertools.product(["R", "G", "B", "Y", "P", "O"], repeat=4)
        # A LR é uma lista de arrays, aqui o JOIN transforma em string
        self.all_answers = {"".join(answer) for answer in self.all_answers}
        # Quantidade padrão para o jogo Mastermind, mesmo sabendo que não será necessário toda essa quantidade
        self.palpites_left = 10
        self.palpite_history = []
        self.hint_history = []
        self.answer = answer

        FileStore = open("storage/dicionario_resultados.pickle", "rb")
        self.score_dict = pickle.load(FileStore)
        FileStore.close()

    def make_palpite(self):
        palpites_to_try = []
        for palpite, scores_by_answer_dict in self.score_dict.items():
            # Filtra para incluir apenas as respostas possíveis
            scores_by_answer_dict = {answer: score for answer, score in scores_by_answer_dict.items()
                                     if answer in self.all_answers}
            self.score_dict[palpite] = scores_by_answer_dict

            # Faz a contagem de cada um dos valores obtidos, Ex: {"BBB": 10, "B": 7, "BW": 20}
            possibilities_per_score = collections.Counter(scores_by_answer_dict.values())
            # Procura pelo pior caso, procurando qual o valor que mais se repete, no caso do Ex anterior será 20
            pior_caso = max(possibilities_per_score.values())

            # É preferível palpites possíveis em vez dos impossíveis
            palpite_impossivel = palpite not in self.all_answers
            palpites_to_try.append((pior_caso, palpite_impossivel, palpite))

        # Quem vai determinar qual o próximo palpite é o minimo, temos um array de array
        # Ex: [(72, True, 'RRRR'), (64, True, 'RRRG'), (42, True, 'RRRB'),...]
        # Se o primeiro valor for igual, o segundo é quem vai desempatar,
        # nesse caso a função dá prioridade para o FALSE, ou seja, para valores possíveis.
        # Mas terão momentos em que serão utilizados palpites impossíveis.
        test = min(palpites_to_try)
        test2 = test[-1]
        return test2

    def solve(self):
        while self.palpites_left > 0:
            if self.palpites_left == 10:
                palpite = "RRGG"
            else:
                palpite = self.make_palpite()

            self.palpite_history.append(palpite)

            score = score_guess(palpite, self.answer)
            self.hint_history.append(score)
            # Filtro em busca apenas dentro da chave do palpite pelos valores iguais ao resultado
            self.all_answers = {answer for answer in self.all_answers
                                if self.score_dict[palpite][answer] == score}

            self.palpites_left -= 1
            if palpite == self.answer:
                return self.palpite_history, self.hint_history