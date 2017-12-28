#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jack Xie'

class Settings():
    """存储《外星人入侵》的所有设置"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 640
        self.screen_height = 960
        self.bg_color = (230, 230, 230)

        # 飞船的设置  (值为0.5时不能够向右和向下移动 ？？？)
        self.ship_speed_factor = 1.5


















