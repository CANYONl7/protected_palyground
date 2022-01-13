'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-21
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

import pygame

from pygame.sprite import Sprite

#运动员设置
class Athlete(Sprite):
    #初始化运动员并使其复位
    def __init__(self,ai_game):
        super().__init__()

        self.screen      = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings    = ai_game.settings 

        #加载图片并将其外形近似为矩形
        self.image = pygame.image.load('images/athlete.png')
        self.rect  = self.image.get_rect()

        #加载后将其居中self.screen_wide = 1200
        self.rect.midbottom = self.screen_rect.midbottom

        #存储小数值
        self.x = float(self.rect.x)

        #移动标识
        self.moving_right = False
        self.moving_left  = False

    #根据移动标识实现移动
    def update(self):
        #限制活动范围
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.athlete_speed
        if self.moving_left  and self.rect.left  > 0 :
            self.x -= self.settings.athlete_speed
        self.rect.x = self.x

    #在指定位置显示运动员
    def blitime(self):
        self.screen.blit(self.image , self.rect)

    #将运动员居中
    def center_athlete(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x              = float(self.rect.x)