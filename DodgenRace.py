import pygame
import time
import random
pygame.init()
display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
block_color = (255, 128, 0)
green = (0, 200, 0)
red = (200, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Dodge n' Race")
car_img = pygame.image.load("racecar.png")
def car_image(x, y):
    screen.blit(car_img, (x, y))
def game_quit():
    pygame.quit()
    exit()
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if mouse[0] >= x and mouse[0] <= x+w and mouse[1] >= y and mouse[1] <= y+h:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    small_text = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(msg, small_text)
    TextRect.center = ((x+w/2, y+h/2))
    screen.blit(TextSurf, TextRect)
def scoreboard(count):
    font = pygame.font.Font("freesansbold.ttf", 25)
    text = font.render("Score: "+str(count), True, black)
    screen.blit(text, (0, 0))
def object(object_x, object_y, object_width, object_height, color):
    pygame.draw.rect(screen, color, pygame.Rect(object_x, object_y, object_width, object_height))
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def display_message(text):
    largeText = pygame.font.Font("freesansbold.ttf", 110)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2, display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
def crash():
    display_message("You crashed")
def intro():
    intro = False
    while not intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill(white)
        midText = pygame.font.Font("freesansbold.ttf", 80)
        TextSurf, TextRect = text_objects("Dodge n' Race", midText)
        TextRect.center = ((display_width/2, display_height/2))
        screen.blit(TextSurf, TextRect)
        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, game_quit)
        pygame.display.update()
        clock.tick(15)
def game_loop():
    x = display_width * 0.3
    y = display_height * 0.6
    object_width = 100
    object_height = 100
    object_x = random.randint(0, display_width-object_width)
    object_y = -600
    object_speed = 4
    count = 0
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 5
        if pressed[pygame.K_RIGHT]:
            x += 5
        screen.fill(white)
        car_image(x, y)
        object(object_x, object_y, object_width, object_height, block_color)
        scoreboard(count)
        if x > display_width-324+145 or x < -130:
            crash()
        if x+324-145 >= object_x and x+130 <= object_x+object_width and y+130 <= object_y+object_height:
            crash()
        if object_y > display_height:
            object_y = -object_height
            object_x = random.randint(0, display_width - object_width)
            count += 1
            if count%5 == 0 and count <= 50:
                object_speed += 1
            elif count%10 == 0 and count <= 100:
                object_speed += 1
            elif count%20 == 0 and count > 100:
                object_speed += 1
        object_y += object_speed
        pygame.display.update()
        clock.tick(60)
intro()
game_loop()
pygame.quit()
exit()