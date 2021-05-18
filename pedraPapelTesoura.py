import random
from time import sleep

print('Jogo Pedra, Papel, Tesoura:')

tecla = input('Para ver regras digite r e depois ENTER >: ').lower()

if tecla == 'r':
    print('Regras:')
    print('Pedra vence Tesoura')
    print('Tesoura vence papel')
    print('Papel vence pedra')

jogadorAI = ['pedra', 'papel', 'tesoura']

objetos = []
        # 1: pedra, 2:tesoura, 3:papel

while True:
    print('Digite pedra, papel ou tesoura')
    objetos.append(input('>: '))
    objetos.append(jogadorAI[random.randint(0, 2)])
    print('1....2.....3......e.....JÁ....')
    sleep(1)

    if objetos[0] == objetos[1]: print('Empate')
    elif objetos[0] == 'pedra' and objetos[1] == 'tesoura': print('Pedra vence tesoura')
    elif objetos[0] == 'tesoura' and objetos[1] == 'pedra': print('Pedra vence tesoura')
    elif objetos[0] == 'tesoura' and objetos[1] == 'papel': print('Tesoura vence papel')
    elif objetos[0] == 'papel' and objetos[1] == 'tesoura': print('Tesoura vence papel')
    elif objetos[0] == 'papel' and objetos[1] == 'pedra': print('Papel vence pedra')
    elif objetos[0] == 'pedra' and objetos[1] == 'papel': print('Papel vence pedra')
    print(objetos)
    objetos.clear()


