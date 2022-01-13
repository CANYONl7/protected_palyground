'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-25
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

import pygame.font    #pygame.font将文本渲染到屏幕上

class Button:
    #初始化按钮属性
    def __init__(self,ai_game,msg):
        self.screen      = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width,self.height = 200,50
        self.button_color      = (252,221,225)
        self.text_color        = (120,120,120)
        self.font              = pygame.font.SysFont(None,48)    #None默认字体
        #创建实参并使其居中
        self.rect        = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    #将msg渲染为图像
    def _prep_msg(self,msg):
        #font.render完成文本到图像的转换并将其存储
        self.msg_image             = self.font.render(msg,True,self.text_color,self.button_color)   #布尔实参判断是否开启反锯齿功能
        self.msg_image_rect        = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    #绘制按钮
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)            #填充颜色
        self.screen.blit(self.msg_image,self.msg_image_rect)     #绘制文本