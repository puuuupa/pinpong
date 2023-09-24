#Создай собственный Шутер!
from time import time as timer
from pygame import *
from random import randint
mixer.init()
font.init()




window = display.set_mode((700,500))
window.fill((255, 255, 224))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y,player_x, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.y = player_y
        self.rect.x = player_x
    
    def reset(self):
        window.blit(self.image, self.rect)

class PLayer(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed       
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed       
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed         




myach = GameSprite('myach.png',230,320,50,50,50)
raketka1 = PLayer('zxc.png',210,10,170,140,10)


raketka2 = PLayer('zxc.png',210,530,170,140,10)
mixer.music.load('topsong.mp3')
#mixer.music.play(-1)
mixer.music.set_volume(0.1)





while True:
    window.fill((255, 255, 224))
    for i in event.get():
        if i.type == QUIT:
            exit()

    myach.reset()
    raketka1.update()
    raketka1.reset()
 
    raketka2.update1()
    raketka2.reset()

    display.update()
    time.delay(15)










