'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-26
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

import pygame

#背景管理
class Foreground:
    #初始化背景设置
    def __init__(self , ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/foreground.png')
        self.rect  = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image , self.rect)