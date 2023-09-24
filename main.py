import pygame
from random import randint
from time import time

width = 1300
height = 700

FPS = 60

window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.display.set_caption("Гра Пінг Понг,Автор:Владислав Височан")

background = pygame.transform.scale(
    pygame.image.load("field.png"),
    (width,height)
)

background_color = (253, 253, 3)

pygame.font.init()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x,y, speed, size):
        super().__init__()
        self.image = pygame.transform.scale(
                            pygame.image.load(image),
                            size                            
        )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))



class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < height-200:
            self.rect.y += self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < height-200:
            self.rect.y += self.speed

ball = GameSprite("ball.png", width/2, height/2, 0, (50,50))

racket_1 = Player("racket.png", 10, height/2-50, 7, (50,200))
racket_2 = Player("racket.png", width-60, height/2-50, 7, (50,200))

score_1 = 0
score_2 = 0

speed_x = 5
speed_y = 5

font2 = pygame.font.Font(None, 50)

game_over = False
finish = False

while not game_over:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
                game_over = True

    if not finish:
    
        #window.fill(background_color)
        window.blit(background, (0,0))

        score_1_text = font2.render(str(score_1), True, (100,0,0))
        score_2_text = font2.render(str(score_2), True, (100,0,0))

        window.blit(score_1_text, (100,100))
        window.blit(score_2_text, (width-100,100))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > height-50 or ball.rect.y < 0:
            speed_y = speed_y * (-1)

        if pygame.sprite.collide_rect(ball, racket_1) or pygame.sprite.collide_rect(ball, racket_2):
           speed_x *= -1
        
        if ball.rect.x > width-50:
           score_1 += 1
           ball.rect.x = width/2
           ball.rect.y = height/2

        if ball.rect.x < 0:
           score_2 += 1
           ball.rect.x = width/2
           ball.rect.y = height/2


        if score_1 >= 5:
            font = pygame.font.Font(None, 50)
            text_win = font.render("Переміг гравець 1", True, (255,95,1))
            window.blit(text_win, (width/2-70,height/2-20))
            finish = True

        if score_2 >= 5:
            font = pygame.font.Font(None, 50)
            text_win = font.render("Переміг гравець 2", True, (255,95,1))
            window.blit(text_win, (width/2-70,height/2-20))
            finish = True

        ball.reset()

        racket_1.reset()
        racket_2.reset()

        racket_1.update_l()
        racket_2.update_r()

    pygame.display.update()
    clock.tick(FPS)