import collections
import itertools
import pickle


def score_guess(palpite, resposta):
    # Iteração item a item para determinar o resultado entre o palpite e a resposta
    hints = []
    ans_no_match = []
    guess_no_match = []
    # Quebra a string em pedaços, Ex: RRRR, GBYG -> ["R", "R", "R", "R"], ["G", "B", "Y", "G"]
    # fazendo a iteração entre cada um dos itens
    for guess_elem, ans_elem in zip(palpite, resposta):
        if guess_elem == ans_elem:
            hints.append("B")
        else:
            guess_no_match.append(guess_elem)
            ans_no_match.append(ans_elem)

    for guess_elem in guess_no_match:
        if guess_elem in ans_no_match:
            hints.append("W")
            ans_no_match.remove(guess_elem)

    return "".join(hints)


def build_dict():
    # Cria o estrutura do tipo dicionário
    score_dict = collections.defaultdict(dict)
    # Faz a iteração entre todas as variáveis, Ex: RRRR, RRRG, ..., RGBY, ..., OOOP, OOOO
    all_guesses = itertools.product(["R", "G", "B", "Y", "P", "O"], repeat=4)

    for guess, answer in itertools.product(all_guesses, repeat=2):
        guess_str = "".join(guess)
        ans_str = "".join(answer)
        # Armazena os dados como um objeto,
        # Ex: RRRR: { RRRR: "BBBB", RRRG: "BBB", ..., OOOO: ""}, ..., RGBY: { RRRR: "B", RRRG: "BW", ..., OOOO: ""}
        score_dict[guess_str][ans_str] = score_guess(guess, answer)

    # Salva o Dicionário em um arquivo para evitar o consumo de tempo e memória todas as vezes em que iniciar o jogo
    FileStore = open("storage/dicionario_resultados.pickle", "wb")
    pickle.dump(score_dict, FileStore)
    FileStore.close()


if __name__ == "__main__":
    build_dict()
