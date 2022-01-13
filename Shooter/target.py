'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-22
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

import pygame
from pygame import sprite

from pygame.sprite import Sprite

#表示单个目标的类
class Target(Sprite):
    #初始化目标并将其置于初始位置
    def __init__(self,ai_game):
        super().__init__()
        self.screen   = ai_game.screen
        self.settings = ai_game.settings

        #加载图像并设置其rect属性
        self.image = pygame.image.load('images/redbird.png')
        self.rect  = self.image.get_rect()

        #初始位置为左上
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        #存储准确水平位置
        self.x = float(self.rect.x)

    #边缘检测
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right  or  self.rect.left <= 0:
            return True     #若位于边缘则返回True

    #目标平移
    def update(self):
        self.x     += (self.settings.target_speed * self.settings.fleet_direction)
        self.rect.x = self.x