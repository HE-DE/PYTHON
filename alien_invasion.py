import sys

import pygame

from settings import Settings

from ship import Ship


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
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监视鼠标和键盘事件
        # 如果鼠标点击退出则退出程序
        for event in pygame.event.get():  # event.get()访问pygame检测到的事件
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环重绘屏幕
        screen.fill(ai_settings.bg_color)  # 调用fill方法用背景色填充整个屏幕

        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
