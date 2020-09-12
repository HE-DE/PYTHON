# 用于存放该项目的全部设置文件
# 创建Settings类

class Settings():
    """存储该项目的所有类"""

    def __init__(self):
        """初始化游戏设置（构造函数）"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_facter = 1.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
