import re
from prettytable import PrettyTable
from mastermind_solver import MastermindCodeBreaker


def is_color(val):
    length = len(val)
    pattern = r"[RGBYPO]{1}"
    regex = bool(re.match(pattern, val, re.I))
    return length == 1 & regex


def wait_input(i):
    x = input(f"Cor na posição ${i + 1}: ")
    x = x.upper()
    if is_color(x):
        return x
    else:
        print("Você digitou uma cor diferente da esperada.")
        return wait_input(i)


def loopInput():
    color_string = ''
    for i in range(4):
        color_string += wait_input(i)

    return color_string


def make_table(senha, palpites, resultados):
    table = PrettyTable()
    table.title = f"A senha escolhida foi: {senha}"
    table.add_column("Palpites", palpites)
    table.add_column("Resultados", resultados)
    return table


print("Crie uma senha com 4 cores")
print("As cores disponíveis são: ")
print("        R => Vermelho")
print("        G => Verde")
print("        B => Azul")
print("        Y => Amarelo")
print("        P => Roxo")
print("        O => Laranja")
color_array = loopInput()
array_result = MastermindCodeBreaker(color_array).solve()
print(make_table(color_array, array_result[0], array_result[1]))
