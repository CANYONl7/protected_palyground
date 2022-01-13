'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-25
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

import pygame.font

from pygame.sprite import Group
from athlete       import Athlete

#计分板
class Scoreboard:
    #初始化相关属性
    def __init__(self,ai_game):
        self.ai_game     = ai_game
        self.screen      = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings    = ai_game.settings
        self.stats       = ai_game.stats
        #字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_athletes()


    #将得分转化为图像
    def prep_score(self):
        #以10位最小整数倍将得分取整
        rounded_score            = round(self.stats.score , -1)             #round()第二个实参为负时舍入为10^x的整数倍
        #先转化为字符串
        score_str                = "{}""{:,}".format("SCORE:",rounded_score)               #在分数中插入逗号
        self.score_image         = self.font.render(score_str , True , self.text_color , self.settings.bg_color)
        #在窗体右上显示得分
        self.score_rect                 = self.score_image.get_rect()
        self.score_rect.right           = self.screen_rect.right - 20
        self.score_rect.top             = 10

    #将最高分转化为图像
    def prep_highest_score(self):
        #以10位最小整数倍将得分取整
        highest_score            = round(self.stats.highest_score , -1)     #round()第二个实参为负时舍入为10^x的整数倍
        #先转化为字符串
        highest_score_str        = "{}""{:,}".format("H-SCORE:",highest_score)             #在分数中插入逗号
        self.highest_score_image = self.font.render(highest_score_str , True , self.text_color , self.settings.bg_color)
        #在顶部中央显示最高分
        self.highest_score_rect         = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top     = self.screen_rect.top + 10

    #刷新最高分
    def check_highest_score(self):
        if self.stats.score > self.stats.highest_score:
            self.stats.highest_score = self.stats.score
            self.prep_highest_score()

    #将等级转化为图像
    def prep_level(self):
        #先转化为字符串
        level_str        = "{}""{:,}".format("LEVEL:",self.stats.level)
        self.level_image = self.font.render(level_str , True , self.text_color , self.settings.bg_color)
        #在窗体右下显示等级
        self.level_rect                = self.level_image.get_rect()
        self.level_rect.left           = self.screen_rect.left + 20
        self.level_rect.top            = 10


    #显示剩余生命
    def prep_athletes(self):
        self.athletes = Group()
        for athlete_number in range(self.stats.athletes_left):
            athlete = Athlete(self.ai_game)
            athlete.rect.x = 1400 
            athlete.rect.y = 710 - athlete_number * athlete.rect.width
            self.athletes.add(athlete)


    #显示数据
    def show_score(self):
        self.screen.blit(self.score_image         , self.score_rect        )
        self.screen.blit(self.highest_score_image , self.highest_score_rect)
        self.screen.blit(self.level_image         , self.level_rect        )
        self.athletes.draw(self.screen)