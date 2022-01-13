'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-24
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

import json

#追踪游戏的统计信息
class GameStats:
    #初始化静态统计信息
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        #控制游戏活跃部分状态
        self.game_active = False
        #固定并存储最高分
        self.highest_score = 0

    #初始化动态统计信息
    def reset_stats(self):
        self.athletes_left = self.settings.athlete_limit

        self.score = 0
        self.level = 1 