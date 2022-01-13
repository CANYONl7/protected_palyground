'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-20
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

#管理功能与设置
class Settings:
    
    #初始化游戏静态设置
    def __init__(self):
        #屏幕设置
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color      = (150,190,230)

        #运动员设置
        self.athlete_limit = 2

        #子弹设置
        self.bullet_width   = 4
        self.bullet_height  = 20
        self.bullet_color   = (60,60,60)
        self.bullet_allowed = 5

        #目标设置
        self.fleet_drop_speed = 10

        #加快游戏节奏
        self.speedup_scale = 1.3
        #目标分值提升
        self.score_scale   = 1.5

        self.initialize_dynamic_settings()

    #初始化游戏动态设置
    def initialize_dynamic_settings(self):
        self.athlete_speed = 5
        self.bullet_speed  = 10
        self.target_speed  = 5

        self.fleet_direction  = 1   #1表示右移，-1表示左移

        #得分
        self.target_points = 50

    #时序激励
    def increase_speed(self):
        #加速
        self.athlete_speed *= self.speedup_scale
        self.bullet_speed  *= self.speedup_scale
        self.target_speed  *= self.speedup_scale
        #提分
        self.target_points  = int(self.target_points * self.score_scale)