import pygame


pygame.init() #auto explicativo kkkk começar a rodar o pygame


window = pygame.display.set_mode([1280, 720]) #criei uma variavel com o tamanho da janela do jogo
title = pygame.display.set_caption("Pong") #uma variavel p/ titulo

win = pygame.image.load("sprites/assets/win.png")

score1 = 0
score1_img = pygame.image.load("sprites/assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("sprites/assets/score/0.png")

scenario = pygame.image.load("sprites/assets/field.png") #variavel p/ cenario(fundo), pega o arquivo de outra pasta

player1 = pygame.image.load("sprites/assets/player1.png")
player1_x = 50
player1_y = 287
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("sprites/assets/player2.png")
player2_x = 1150
player2_y = 287

ball = pygame.image.load("sprites/assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -5
ball_dir_y = 1

bar = pygame.image.load("sprites/assets/bar.png")


def move_player():
    global player1_y
    global player1_moveup
    global player1_movedown

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y -= 0

    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0
    
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

def move_player2():
    global player2_y
    player2_y = ball_y


def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score2_img
    global score1_img

    ball_x += ball_dir
    ball_y += ball_dir_y

    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1

    if ball_x > 1110:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1
    
    if ball_y > 675:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load("sprites/assets/score/" + str(score2) + ".png")

    if ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load("sprites/assets/score/" + str(score1) + ".png")

def draw():
    if score1 or score2 < 9:
        window.blit(scenario, (0, 0)) #p/ adicionar uma imagem na janela do jogo
        window.blit(player1, (player1_x, player1_y)) #adicionar sprite do player1
        window.blit(player2, (player2_x, player2_y)) #adicionar sprite do player2
        window.blit(ball, (ball_x, ball_y)) #adicionar sprite da bola
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(win, (300, 330))

loop = True #variavel para deixar o programa aberto (até ser fechado)
while loop:

    for events in pygame.event.get(): #para cada evento que tiver dentro do "pygame.event.get()"
        if events.type == pygame.QUIT: #se o tipo do evento for igual a "pygame.QUIT"(X para fechar) então
            loop = False #se encerra a janela
        if events.type == pygame.KEYDOWN: #se o tipo do evento for "tecla pressionada"
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP: #se o tipo do evento for "tecla pressionada"
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

    draw()
    pygame.display.update()