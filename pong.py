import pygame


pygame.init() #initializes Pygame

window = pygame.display.set_mode([1280, 720]) #created a variable with the size of the game window
title = pygame.display.set_caption("Pong") #a variable for title

win = pygame.image.load("sprites/assets/win.png")

score1 = 0
score1_img = pygame.image.load("sprites/assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("sprites/assets/score/0.png")

scenario = pygame.image.load("sprites/assets/field.png") #variable for scenery (background), takes the file from another folder

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
        window.blit(scenario, (0, 0)) #to add an image to the game window
        window.blit(player1, (player1_x, player1_y)) #add player1 sprite
        window.blit(player2, (player2_x, player2_y)) #add player2 sprite
        window.blit(ball, (ball_x, ball_y)) #add ball sprite
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(win, (300, 330))

loop = True #variable to leave the program open (until closed)
while loop:

    for events in pygame.event.get(): #for each event inside "pygame.event.get()"
        if events.type == pygame.QUIT: #if the event type is equal to "pygame.QUIT"(X to close) then
            loop = False #closes the window
        if events.type == pygame.KEYDOWN: #if the event type is "key pressed"
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP: #if the event type is "key released"
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

    draw()
    pygame.display.update()
