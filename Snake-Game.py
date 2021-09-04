''' Snake and apple game ---->
Snake and apple game is my one of the favorite game of past.

Coded By: Sonu Shriram Vishwakarma(FD23)

'''

# Modules ---->

import pygame
import random
import time

# Intitializing all display modules of pygame---->

pygame.init()

#  All variables related to games are here---->


display_x = 800
display_y = 500
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
#width_Of_Head = 15
#lenth_Of_Head = 15



#head = [head_x, head_y, lenth_Of_Head, width_Of_Head]
# Functions required for game--->

def snake_increment(snake_list, snake_body):
    for x, y in snake_list:
        pygame.draw.rect(screen, yellow, [x, y, snake_body, snake_body])
def score(score):
    font = pygame.font.Font("freesansbold.ttf", 20)
    
    font_dis = font.render("Score: "+str(score), True, (255, 0, 0))
    font_disRect = font_dis.get_rect()
    font_disRect.left
    screen.blit(font_dis, font_disRect)

def end(quit):
    font = pygame.font.Font("freesansbold.ttf", 20)
    
    font_dis = font.render(quit, True, (255, 0, 0))
    font_disRect = font_dis.get_rect()
    font_disRect.centerx
    screen.blit(font_dis, font_disRect)
def over_window(loop_end):
    while loop_end:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            loop_start()
                        if event.key == pygame.K_q:
                            loop_end = False
                            return False  
                    if event.type == pygame.QUIT:
                        loop_end = False
                        return False   

def move():
    play_sound = pygame.mixer.Sound("move.mp3") 
    play_sound.play()  
def food():
    play_sound = pygame.mixer.Sound("food.mp3") 
    play_sound.play()  
def gameover():
    play_sound = pygame.mixer.Sound("gameover.mp3") 
    play_sound.play()        
def music():
    play_sound = pygame.mixer.Sound("music.mp3") 
    play_sound.play(-1) 
    
#help(pygame.font.Font)
# Display properties--->

pygame.display.set_caption("Snake And Apple Game - By Sonu")
screen = pygame.display.set_mode((display_x, display_y))
screen.fill(white)
pygame.display.flip()






# Game loop----->
def loop_start():
    display_x = 800
    display_y = 500
    loop = True
    snake_body = 20
    head_x = 700
    head_y = 400
    width_Of_apple = 20
    lenth_Of_apple = 20
    apple_x = random.randint(25, (display_x-25))
    apple_y = random.randint(50, (display_y-25))

    clock = pygame.time.Clock()
    fps = 30
    velocity_x = 0
    velocity_y = 0
    velocity_value = 8
    score_value = 0
    snake_list = []
    snake_len = 1
    loop_end = True
    #music()
    while loop:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #print("up down") # Only to check
                    velocity_y = -velocity_value
                    velocity_x = 0
                    move() 
                    #head[1] = head_y
                if event.key == pygame.K_DOWN:
                    velocity_y = velocity_value
                    velocity_x = 0
                    move() 
                    #head_y +=25
                    #head[1] = head_y
                if event.key == pygame.K_LEFT:
                    velocity_x = -velocity_value
                    velocity_y = 0
                    move() 
                    #head[0] = head_x
                if event.key == pygame.K_RIGHT:
                    velocity_x = velocity_value
                    velocity_y = 0
                    move() 
                    #head[0] = head_x   
                    
                    #print(head_y) # Check value of head is decresing or not                
                
            
            
            
            
    
            # Condition of game quite
            if event.type == pygame.QUIT:
                loop = False
                
        head_x = head_x + velocity_x   
        head_y = head_y + velocity_y
        
        if abs(head_x-apple_x)<15 and abs(head_y-apple_y)<15: 
            apple_x = random.randint(25, (display_x-25))
            apple_y = random.randint(50, (display_y-25))
            score_value += 10
            snake_len = len(snake_list)+5
            food()
            #print(snake_len)    
            
            #print(score)
           
        # appending x and y coordinates from head_x and head_y
        head_snake = []
        head_snake.append(head_x)   
        head_snake.append(head_y)
        snake_list.append(head_snake) 
        #print(snake_list)
        #print("Snake length is : ",snake_len)
        
        
            
        if len(snake_list)>snake_len:
            #print(len(snake_list))
            del snake_list[0]   
        if head_x<0 or head_y<0 or head_x>display_x or head_y>display_y:
            #print("true")
            gameover()
            screen.fill(white)
            end("Press 'Space' to continue or press 'Q' to quit")
            pygame.display.flip()
            loop =  over_window(loop_end)
        if head_snake in snake_list[:-1]:
            gameover()
            screen.fill(white)
            end("Press 'Space' to continue or press 'Q' to quit")
            pygame.display.flip()
            loop =  over_window(loop_end)
                      
                
        
            
        
        screen.fill(white)
        score(score_value)
        
        #snake_head = pygame.draw.rect(screen, yellow, [head_x, head_y, lenth_Of_Head, width_Of_Head])
        snake_increment(snake_list, snake_body)
        
        apple = pygame.draw.rect(screen, red, [apple_x, apple_y, lenth_Of_apple, width_Of_apple]) 
        
        #print(snake_head) 
        #print(head_y) 
        #print(head)
        clock.tick(fps) 
        pygame.display.flip()

    pygame.quit()
    quit()
loop_start()
quit()
