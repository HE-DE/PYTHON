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
