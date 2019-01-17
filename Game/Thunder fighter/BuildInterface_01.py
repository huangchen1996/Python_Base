import pygame
from pygame.locals import *
import time
import random

class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 500
        self.screen = screen_temp
        # 创建一个飞机图片
        self.image = pygame.image.load("./feiji/hero1.png")
        #存储发射子弹对象的引用
        self.bullet_list = []


    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()


    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

'''
显示敌机
'''
class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        # 创建一个飞机图片
        self.image = pygame.image.load("./feiji/enemy0.png")
        #存储发射子弹对象的引用
        self.bullet_list = []
        self.direction = "right"


    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move(self):

        if self.direction=="right":
            self.x += 1
        elif self.direction == "left":
            self.x -= 5

        if self.x > 200:
            self.direction = "left"
        elif  self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 8 or random_num == 20:
         self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 20
        self.y = y - 20
        self.screen = screen_temp
        # 创建一个飞机图片
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5


class EnemyBullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 25
        self.y = y + 40
        self.screen = screen_temp
        # 创建一个飞机图片
        self.image = pygame.image.load("./feiji/bullet1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5


def key_control(hero_temp):
    for event in pygame.event.get():
        # print(event.type)
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()

                # 控制飞机让其向左移动
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()

            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

'''
1,搭建界面，主要完成窗口和背景图的显示
'''
def main():
    #1,创建窗口
    screen = pygame.display.set_mode((450, 700), 0, 32)

    #2，创建一个背景图片
    background = pygame.image.load("./feiji/Background.png")

    #3，创建了一个飞机对象
    hero = HeroPlane(screen)

    #4，创建一架敌机
    enemy = EnemyPlane(screen)



    while True:
        screen.blit(background, (0,0))
        hero.display()
        enemy.display()
        enemy.move()#调用敌机的移动方法
        enemy.fire()#敌机开火
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()



