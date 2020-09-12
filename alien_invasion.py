import sys

import pygame

from settings import Settings

from ship import Ship

from game_functions import check_events

from game_functions import update_screen

from game_functions import update_bullets

from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景设置
    # 调用pygame.display.set_mode创建一个名为screen的显示窗口
    #screen = pygame.display.set_mode((1200, 800))

    # 创建一个Settings对象，将参数进行替换
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 设置背景色
    # bg_color = (230, 230, 230)  # RGB编码指定颜色，将背景颜色设置成浅灰色

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)

    bullets = Group()

    # 开始游戏主循环
    while True:

        check_events(ai_settings, screen, ship, bullets)
        ship.update()
        update_bullets(bullets)
        update_screen(ai_settings, screen, ship, bullets)


run_game()
