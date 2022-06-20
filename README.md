# PAA Trabalho Final - 2022.1
## Decifrando o Mastermind
### Reinaldo Neto

Resumo:   Mastermind é um jogo de tabuleiro, jogado por duas pessoas. Uma é responsável por criar uma senha de cores enquanto o outro tenta decifrá-la, utilizando-se de estratégias e técnicas para solucionar em uma menor quantidade de palpites possíveis. Este trabalho visa provar que o Mastermind é um Problema NP-Completo, mostra soluções já implementadas e propõe uma solução para o problema em forma de algoritmo.

Como jogar:

- Rode o arquivo "main.py"
- No terminal irá aparecer:
```
Crie uma senha com 4 cores
As cores disponíveis são: 
        R => Vermelho
        G => Verde
        B => Azul
        Y => Amarelo
        P => Roxo
        O => Laranja
Cor na posição $1: 
```
- Você deve digitar apenas uma das letras de acordo com a posição que você deseja
```
Cor na posição $1: o
Cor na posição $2: r
Cor na posição $3: y
Cor na posição $4: b
```

- O algoritmo irá fazer as jogadas e no final deverá retornar:

```
+-----------------------------+
| A senha escolhida foi: ORYB |
+-------------+---------------+
|   Palpites  |   Resultados  |
+-------------+---------------+
|     RRGG    |       B       |
|     BBGO    |       WW      |
|     OPOG    |       B       |
|     RYOB    |      BWWW     |
|     ORYB    |      BBBB     |
+-------------+---------------+
```