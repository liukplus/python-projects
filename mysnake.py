import pygame, sys, random, time
from pygame.font import SysFont
from pygame.locals import *
class Point():
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row=row
        self.col=col
    def copy(self):
        return Point(row=self.row,col=self.col)
pygame.init()
white = pygame.Color(255, 144, 20)
init_background = pygame.image.load("background.jpg")
width=800
height=700
window = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
pygame.display.set_caption("Greedy snake!")
ROW = 30
COL = 40
head = Point(row = int(ROW/2),col=int(COL/2))
snake = [Point(row=head.row,col=head.col+1),
        Point(row=head.row,col=head.col+2),
        Point(row=head.row,col=head.col+3)]
head_color = pygame.Color(0,158,128)
snakeFood_color = pygame.Color(28,56,20)
snake_color = pygame.Color(200,147,158)
def newfood():
    while 1:
        new_Food = Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
        if(new_Food.row!=head.row and new_Food.row!=head.row):
            break
    return new_Food
snakeFood = newfood()
def rect(point,color):
    top = point.row*height/ROW
    left = point.col*width/COL
    pygame.draw.rect(window,color,(left,top,width/COL,height/ROW))
rect(head,head_color)
rect(snakeFood,snakeFood_color)
clock = pygame.time.Clock()
def GameOver(window):
    font = pygame.font.SysFont("MicrosoftYaHei",16)
    color = font.render('Game over',True,(150,50,50))
    location = color.get_rect()
    location.midtop = (400,200)
    window.blit(color,location)
    time.sleep(5)
    pygame.quit()
    sys.exit()

direction = 'left'
speed = 8
while True:
    clock.tick(speed)
    window.fill(white)
    for body in snake:
        rect(body,snake_color)
    rect(snakeFood,snakeFood_color)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            GameOver(window)
        elif event.type==pygame.KEYDOWN:
            if event.key==K_RIGHT or event.key==ord('d'):
                if direction=='up' or direction == 'down':
                    direction = 'right'
            if event.key==K_LEFT or event.key==ord('a'):
                if direction=='up' or direction == 'down':
                    direction = 'left'
            if event.key==K_DOWN or event.key==ord('s'):
                if direction=='left' or direction == 'right':
                    direction = 'down'
            if event.key==K_UP or event.key==ord('w'):
                if direction=='left' or direction == 'right':
                    direction = 'up'
            if event.key == ord('f'):
                speed+=1
            if event.key == ord('v'):
                speed-=1
    eat = head.row==snakeFood.row and head.col==snakeFood.col

    if eat:
        snakeFood = newfood()
    else:
        snake.pop()
    snake.insert(0,head.copy())        
    if direction=='left':
        head.col-=1
    if direction=='right':
        head.col+=1
    if direction=='up':
        head.row-=1
    if direction=='down':
        head.row+=1

    if head.col<0 or head.row<0 or head.row>ROW or head.col>COL:
        GameOver(window)
    for body in snake:
        if body.col==head.col and body.row==head.row:
            GameOver(window)
