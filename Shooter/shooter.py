'''
Description :FinalWork
Author      :CANYONl7
Date        :2021-12-20
LastEditTime:2021-12-27
LastEditors :CANYONl7
'''

import sys
from time import sleep     #sleep()撞击后暂停

import pygame
from pygame.mixer import Sound

from athlete    import Athlete
from background import Background
from settings   import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from foreground import Foreground
from button     import Button
from bullet     import Bullet
from target     import Target

#管理游戏资源和行为
class Shooter:
    #初始化游戏并创建资源
    def __init__(self) :
        #初始化背景设置
        pygame.init()
        self.settings = Settings()

        #全屏显示
        self.screen                 = pygame.display.set_mode((0,0) , pygame.FULLSCREEN)
        self.settings.screen_width  = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        #创建显示窗口
        pygame.display.set_caption("Shooter")

        self.stats      = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.background = Background(self)
        self.foreground = Foreground(self)

        self.athlete    = Athlete(self)
        self.bullets    = pygame.sprite.Group()
        self.targets    = pygame.sprite.Group()

        self._create_fleet()

        #创建按钮
        self.play_button = Button(self,"PLAY")

        #播放音乐
        pygame.mixer.music.load('music/Vitality mittsies.mp3')
        pygame.mixer.music.play(-1)

        #设置背景色
        self.bg_color = (230,230,230)

    def run_game(self) :
        #游戏主循环
        while True:
            self._check_events()

            if self.stats.game_active:
                self.athlete.update()
                self._update_bullets()
                self._update_targets()

            self._update_screen()

            #屏幕可视化
            pygame.display.flip()


    #监视键鼠事件
    def _check_events(self):
        for event in pygame.event.get():
            #检测是否点击关闭按钮
            if   event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()    #pygame.mouse.get_pos返回一个包含鼠标xy坐标的元组 
                self._check_play_button(mouse_pos)

    #响应开始按钮
    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #播放音效
            pygame.mixer.init()
            sound = pygame.mixer.Sound('music/button.wav')
            sound.play()
            #重置游戏动态数据
            self.settings.initialize_dynamic_settings()
            #重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_athletes()
            #清空屏幕元素
            self.targets.empty()
            self.bullets.empty()
            #重置屏幕元素
            self._create_fleet()
            self.athlete.center_athlete()
            #隐藏光标
            pygame.mouse.set_visible(False)

    #按下按键
    def _check_keydown_events(self,event):
        #检测左右连续移动
        if   event.key == pygame.K_RIGHT:
            self.athlete.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.athlete.moving_left  = True 
        #退出
        elif event.key == pygame.K_q:
            sys.exit()
        #发射子弹
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    #松开按键
    def _check_keyup_events(self,event):
        #检测左右连续移动
        if   event.key == pygame.K_RIGHT:
            self.athlete.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.athlete.moving_left  = False


    def _fire_bullet(self):
        #创建一个编组并将其加入编组bullets中
        if len(self.bullets) < self.settings.bullet_allowed:     #限制最大子弹数目
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            #播放有效
            pygame.mixer.init()
            sound = pygame.mixer.Sound('music/openfrie.wav')
            sound.play()

    #检查子弹与目标是否碰撞
    def _check_bullet_target_collosions(self):
        collisions = pygame.sprite.groupcollide(self.bullets , self.targets , True , True)    #sprite.groupcollide比较两个编组元素并返回一个键为子弹值为击中目标的字典
        if collisions:
            for targets in collisions.values():                                    #遍历字典确保将消灭的每个外星人都计入得分
                self.stats.score += self.settings.target_points * len(targets)     #将每个值（列表）中消灭的目标分值累加
            self.scoreboard.prep_score()             #创建新的得分图像
            self.scoreboard.check_highest_score()    #创建新的最高分图像
        #生成新的目标群
        if not self.targets:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            #升级
            self.stats.level += 1
            self.scoreboard.prep_level()
            #播放音效
            pygame.mixer.init()
            sound = pygame.mixer.Sound('music/levelup.wav')
            sound.play()

    #碰撞响应
    def _athlete_hit(self):
        if self.stats.athletes_left > 0:
            #播放有效
            pygame.mixer.init()
            sound = pygame.mixer.Sound('music/loselife.wav')
            sound.play()
            #生命值减1
            self.stats.athletes_left -= 1
            self.scoreboard.prep_athletes()
            #清空剩余物体
            self.targets.empty()
            self.bullets.empty()
            #重置目标群和运动员
            self._create_fleet()
            self.athlete.center_athlete()
            #暂停
            sleep(0.5)
        else:
            self.stats.game_active = False   #结束游戏
            pygame.mouse.set_visible(True)   #重现光标

    def _update_bullets(self):
        self.bullets.update()
        #删除屏幕外的子弹
        for bullet in self.bullets.copy():      #遍历列表副本从而使其能在循环中被修改
            if bullet.rect.bottom <= 0:         #检测底端数值是否为0
                self.bullets.remove(bullet)
        self._check_bullet_target_collosions()

    #创建第一个目标并将其放置到当前行
    def _create_target(self,target_number , row_number):
        target                     = Target(self)
        target_width,target_height = target.rect.size
        target.x                   = target_width + (target_width * 2) * target_number
        target.rect.x              = target.x
        target.rect.y              = target.rect.height + (target.rect.height *2) * row_number
        self.targets.add(target)
    
    #更新目标群位置
    def _update_targets(self):
        self._check_fleet_edges()
        self.targets.update()
        #检查目标与运动员是否碰撞
        if pygame.sprite.spritecollideany(self.athlete , self.targets):
            self._athlete_hit()
        #检查是否有目标触底
        self._check_targets_bottom()

    #创建目标
    def _create_fleet(self):
        target = Target(self)
        #计算每行可用空间和可容纳的整数目标个数
        target_width,target_height = target.rect.size    #size是一个包含两个属性的元组
        available_space_x = self.settings.screen_width - (target_width * 2)
        number_targets_x  = available_space_x // (target_width * 2)
        #计算可容纳行数
        athlete_height    = self.athlete.rect.height
        available_space_y = (self.settings.screen_height - (target_height * 3) - athlete_height)
        number_rows       = available_space_y // (target_height * 2) 

        #创建目标群
        for row_number in range(number_rows):   #利用嵌套循环先行后列创建目标群
            for target_number in range(number_targets_x):
                self._create_target(target_number , row_number)

    #左右边缘检测反馈
    def _check_fleet_edges(self):
        for target in self.targets.sprites():
            if target.check_edges():
                self._change_fleet_direction()
                break

    #目标群转向
    def _change_fleet_direction(self):
        for target in self.targets.sprites():
            target.rect.y += self.settings.fleet_drop_speed     #下移
        self.settings.fleet_direction *= -1                     #反向

    #底部边缘检测反馈
    def _check_targets_bottom(self):
        screen_rect = self.screen.get_rect()
        for target in self.targets.sprites():
            if target.rect.bottom >= screen_rect.bottom:
                self._athlete_hit()     #处理方式同运动员
                break

    #刷新屏幕
    def _update_screen(self):
        #每次循环时重绘屏幕
        self.screen.fill(self.settings.bg_color)     #fill()只接受一个实参：一种颜色
        self.background.blitme()
        self.athlete.blitime()
        
        #遍历列表绘制子弹
        for bullet in self.bullets.sprites():    #bullets.sprites()返回一个包含编组bullets中所有sprites的列表
            bullet.draw_bullet()
        self.targets.draw(self.screen)

        #显示得分
        self.scoreboard.show_score()

        #非活跃状态绘制内容
        if not self.stats.game_active:
            self.foreground.blitme()
            self.play_button.draw_button()

        pygame.display.flip()


#创建实例并运行
if __name__ == '__main__':
    ai = Shooter()
    ai.run_game()