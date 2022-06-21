import collections
import itertools
import pickle


def resultado_do_palpite(palpite, resposta):
    # Iteração item a item para determinar o resultado entre o palpite e a resposta
    dicas = []
    resposta_sem_equivalencia = []
    palpite_em_equivalencia = []
    # Quebra a string em pedaços, Ex: RRRR, GBYG -> ["R", "R", "R", "R"], ["G", "B", "Y", "G"]
    # fazendo a iteração entre cada um dos itens
    for palpite_elem, resposta_elem in zip(palpite, resposta):
        if palpite_elem == resposta_elem:
            dicas.append("B")
        else:
            palpite_em_equivalencia.append(palpite_elem)
            resposta_sem_equivalencia.append(resposta_elem)

    for palpite_elem in palpite_em_equivalencia:
        if palpite_elem in resposta_sem_equivalencia:
            dicas.append("W")
            resposta_sem_equivalencia.remove(palpite_elem)

    return "".join(dicas)


def build_dict():
    # Cria o estrutura do tipo dicionário
    dicionario_de_resultados = collections.defaultdict(dict)
    # Faz a iteração entre todas as variáveis, Ex: RRRR, RRRG, ..., RGBY, ..., OOOP, OOOO
    lista_de_resultados = itertools.product(["R", "G", "B", "Y", "P", "O"], repeat=4)

    for palpite, reposta in itertools.product(lista_de_resultados, repeat=2):
        palpite_str = "".join(palpite)
        reposta_str = "".join(reposta)
        # Armazena os dados como um objeto,
        # Ex: RRRR: { RRRR: "BBBB", RRRG: "BBB", ..., OOOO: ""}, ..., RGBY: { RRRR: "B", RRRG: "BW", ..., OOOO: ""}
        dicionario_de_resultados[palpite_str][reposta_str] = resultado_do_palpite(palpite, reposta)

    # Salva o Dicionário em um arquivo para evitar o consumo de tempo e memória todas as vezes em que iniciar o jogo
    FileStore = open("storage/dicionario_resultados.pickle", "wb")
    pickle.dump(dicionario_de_resultados, FileStore)
    FileStore.close()


if __name__ == "__main__":
    build_dict()
