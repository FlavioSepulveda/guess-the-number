#   Guess the number
#   Importando a biblioteca random:
import random as rd

start = input('Pronto pra jogar? [Sim] ou [Nao] ')
#   Crie uma saudação pro jogador com as regras:

print('Bem vindo!')
print('-------------- REGRAS: --------------')
print('1. A maquina irá escolher um numero de 1 a 100;')
print('2. Seu objetivo é acertar o valor.')
print('3. Errando 5 vezes  você perde.')
print('<-------------- ------- -------------->')

#  Criando função que gera o jogo-
#  Quando eu for chamada a brincadeira começa:
def guessTheNumber():
    numero = rd.randint(1,100)
    print('Bem vindo ao Guess The Number')
    tentativas = 0

#   Enquanto eu existir vermos se você vai acertar:
    while True:
        guess = int(input('Digite seu numero: '))

        if guess < numero:
            print('Tente um numero maior.')
            tentativas += 1

        elif guess > numero:
            print('Tente um numero menor.')
            tentativas += 1

        elif guess > 100:
            print('Voa baixo jogador.')

        elif guess > 1000:
            print('Esta Brincando muito.')

#   Perdeu playboy
        elif tentativas == 3:
            break

        else:
            print('PARABENS VOCE GANHOU!')

#   Criando o start do game:
if (start == 'Sim') or (start == 'sim') or (start == 'SIM'):
    guessTheNumber()
else:
    print('Ok, quem sabe na proxima. :)')