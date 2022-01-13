'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-23
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

import pygame

from pygame.sprite import Sprite

#管理子弹属性
class Bullet(Sprite):
    
    #在运动员位置创建一个子弹对象
    def __init__(self,ai_game):
        super().__init__()
        self.screen   = ai_game.screen
        self.settings = ai_game.settings
        self.color    = self.settings.bullet_color

        #在(0,0)处创建一个表示子弹的矩形后将其置于正确的位置
        self.rect        = pygame.Rect(0 , 0 , self.settings.bullet_width , self.settings.bullet_height)
        self.rect.midtop = ai_game.athlete.rect.midtop

        #存储子弹位置
        self.y = float(self.rect.y)

    #子弹向上运动
    def update(self):
        self.y     -= self.settings.bullet_speed
        self.rect.y = self.y

    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen , self.color , self.rect)