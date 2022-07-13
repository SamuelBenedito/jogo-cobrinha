from os import remove
from turtle import *
from freegames import square, vector
from time import sleep

p1xy = vector(-200, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(200, 0)
p2aim = vector(-4, 0)
p2body = set()

p3xy = vector(0, 200)
p3aim = vector(0, -4)
p3body = set()


#------------Define a area do jogo(Quadrado que abre o jogo)------------#
def inside(head):
    """Return True if head inside screen."""
    return -300 < head.x < 300 and -300 < head.y < 300


#------------Menssagem de saudação------------#
print()
print('=================================================')
print('         Bem-vindo a Grade de Tron!         ')
print('=================================================')
print('Controles:')
print('Jogador 1 (q/w), Jogador 2 (y/u), Jogador 3 (7/8)')
print('=================================================')

print('Escolha uma das cores disponiveis para a arena: [gray, black, white]')
corbg = input("Digite a cor: ")

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple']
print(f'Escolha uma das cores para os jogadores: {colors}')


#------------Script para fazer o usuario escolhe a cor do personagem------------#
colorPlayer1 = input("Cor Jogador 1: ")
colors.remove(colorPlayer1)
colorPlayer2 = input("Cor Jogador 2: ")
colors.remove(colorPlayer2)
colorPlayer3 = input("Cor Jogador 3: ")
colors.remove(colorPlayer3)


#------------Temporizador para inicio do jogo------------#
sleep(1)
print('Carrengando Jogo...')
sleep(1)
print("3")
sleep(1)  
print("2")
sleep(1)
print("1")
sleep(1)
print("Vai!")


#-----------Define os movimentos dos players-------------#
def draw():
    """Advance players and draw game."""
    
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    p3xy.move(p3aim)
    p3head = p3xy.copy()


#------------Colisão dos players entre eles------------#
    if not inside(p1head) or p1head in p2body:
        print(f"Jogadores {colorPlayer2} e {colorPlayer3} Ganharam!")
        return

    if not inside(p1head) or p1head in p3body:
        print(f"Jogadores {colorPlayer2} e {colorPlayer3} Ganharam!")
        return

    if not inside(p2head) or p2head in p1body:
        print(f"Jogadores {colorPlayer1} e {colorPlayer3} Ganharam!")
        return

    if not inside(p2head) or p2head in p3body:
        print(f"Jogadores {colorPlayer1} e {colorPlayer3} Ganharam!")
        return

    if not inside(p3head) or p3head in p1body:
        print(f"Jogadores {colorPlayer1} e {colorPlayer2} Ganharam!")
        return

    if not inside(p3head) or p3head in p2body:
        print(f"Jogadores {colorPlayer1} e {colorPlayer2} Ganharam!")
        return

    
#------------Colisão do player em si mesmo------------#
    if not inside(p1head) or p1head in p1body:
        print(f"Jogadores {colorPlayer2} e {colorPlayer3} Ganharam!")
        return

    if not inside(p2head) or p2head in p2body:
        print(f"Jogadores {colorPlayer1} e {colorPlayer3} Ganharam!")
        return

    if not inside(p3head) or p3head in p3body:
        print(f"Jogadores {colorPlayer1} e {colorPlayer2} Ganharam!")
        return


#-----------Adiciona o 'corpo' a 'cabeça'-------------#
    p1body.add(p1head)
    p2body.add(p2head)
    p3body.add(p3head)


#------------Adiciona a direção para que os quadrados devem seguir------------#
    square(p1xy.x, p1xy.y, 3, colorPlayer1)
    square(p2xy.x, p2xy.y, 3, colorPlayer2)
    square(p3xy.x, p3xy.y, 3, colorPlayer3)
    update()
    ontimer(draw, 20)


#------------Adiciona as teclas de comando------------#
bgcolor(corbg) #coloca a cor na tela apresetada para jogar.
setup(600, 600, 370, 0) # define o tamanho da arena
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'q')
onkey(lambda: p1aim.rotate(-90), 'w')
onkey(lambda: p2aim.rotate(90), 'y')
onkey(lambda: p2aim.rotate(-90), 'u')
onkey(lambda: p3aim.rotate(90), '7')
onkey(lambda: p3aim.rotate(-90), '8')
draw()
done()


#------------Alterações Realizadas------------#
#Criação do Player 3 - feito

#Escolha de cor do player - feito

#Colisão entre os players e entre eles mesmos - feito

#Adicionado um Temporizador para começar o jogo - feito

#Aterado para o jogador escolher a cor de fundo - feito