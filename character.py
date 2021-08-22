import pygame, time
from pygame.event import Event
from spritesheet import Spritesheet
import math 

###################### Screen handling ##############################
pygame.init()

SCREEN_W , SCREEN_H = (800,600)
canvas = pygame.Surface((SCREEN_W , SCREEN_H))
screen = pygame.display.set_mode((SCREEN_W , SCREEN_H))

###################### Font Handling ##############################
pygame.font.init()
fps_font = pygame.font.SysFont('Arial', 24)
key_font = pygame.font.SysFont('Arial', 60)
char = ""

###################### Character Display handling ##############################

characher_sprite_sheet = Spritesheet("TurnBasedGameMech/Sprites/hero.png")
hero = characher_sprite_sheet.get_sprites()
hero = [pygame.transform.scale(img, (158, 128)) for img in hero]
render_speed = 1/10
"""
def render_hero(state,face,render_speed,):
    characher_sprite_sheet.set_state(state)
                characher_sprite_sheet.set_face("right")
                hero1 = characher_sprite_sheet.get_sprites()
                hero = [pygame.transform.scale(img, (158, 128)) for img in hero1]
"""
###################### Character Movement Handling ##############################

speed = 10
pos_x = (SCREEN_W/2 - 158/2)
pos_y = (SCREEN_H/2 - 128/2)
vertical_vel = 0
running_right,running_left= False, False

def go_right():
    global pos_x 
    pos_x = pos_x + speed
    if pos_x > SCREEN_W - 228/2:
        pos_x = SCREEN_W - 228/2

        
def go_left():
    global pos_x 
    pos_x = pos_x - speed
    if pos_x < - 90/2:
        pos_x = - 90/2

def jump():
    global pos_y
    global vertical_vel
    pos_y = pos_y + vertical_vel

###################### Physics Handling ##############################
prev_time  =  time.time()
dt = 0
FPS = 60
clock = pygame.time.Clock()

###################### Main Loop ##############################
running = True
index = 0

while running:

    ###################### Checking ##############################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        ###################### Keystroke Handling ##############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                char = "D"
                index = 0
                characher_sprite_sheet.set_state("running")
                characher_sprite_sheet.set_face("right")
                render_speed = 1/6
                hero1 = characher_sprite_sheet.get_sprites()
                hero = [pygame.transform.scale(img, (158, 128)) for img in hero1]
                running_right = True
            
            if event.key == pygame.K_a:
                char = "A"
                index = 0
                characher_sprite_sheet.set_state("running")
                render_speed = 1/6
                characher_sprite_sheet.set_face("left")
                hero1 = characher_sprite_sheet.get_sprites()
                hero = [pygame.transform.scale(img, (158, 128)) for img in hero1]
                
                running_left = True
                
            if event.key == pygame.K_s:
                char = "S"
                index = 0
                characher_sprite_sheet.set_state("crouching")
                render_speed = 1/10
                hero1 = characher_sprite_sheet.get_sprites()
                hero = [pygame.transform.scale(img, (158, 128)) for img in hero1]
                
                
            if event.key == pygame.K_SPACE:
                char = "SPACE"
                index = 0
                characher_sprite_sheet.set_state("jumping")
                render_speed = 1/6
                hero1 = characher_sprite_sheet.get_sprites()
                hero = [pygame.transform.scale(img, (158, 128)) for img in hero1]

            if event.key == pygame.K_o:
                char = "O"
                index = 0
                characher_sprite_sheet.set_state("attacking")

            

            

        if event.type == pygame.KEYUP:
            char = ""
            index = 0
            characher_sprite_sheet.set_state("idle")
            hero1 = characher_sprite_sheet.get_sprites()
            render_speed = 1/10
            hero = [pygame.transform.scale(img, (158, 128)) for img in hero1] 
            if event.key == pygame.K_d:
                running_right = False
            
            if event.key == pygame.K_a:
                running_left = False

                
            if event.key == pygame.K_s:
                pass
                    
            if event.key == pygame.K_SPACE:
                pass
    

    canvas.fill((255,255,255))
    screen.blit(canvas,(0,0))
    
    ###################### Display Texts ##############################
    # FPS
    fps = str(int(clock.get_fps()))
    textsurface = fps_font.render(f'{fps}', False, (0, 0, 0))
    screen.blit(textsurface,(10,10))

    # Pressed Key
    pressed_key = key_font.render(f'{char}', False, (0, 0, 0))
    screen.blit(pressed_key,(SCREEN_W/2,SCREEN_H*0.2))

    ###################### Physics ##############################

    if running_right:
        go_right()
    elif running_left:
        go_left()

    clock.tick(FPS)
    index = (index + render_speed) % len(hero)
    screen.blit(hero[math.floor(index)],(pos_x , pos_y))
    print(str(pos_x) + " " + str(pos_y))
    pygame.display.update()
    
