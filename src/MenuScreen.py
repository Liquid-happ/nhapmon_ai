import sys
import os
import pygame
import pygame_menu
from src.config import *


class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        # Setting menu background
        self.bg = pygame.transform.scale(pygame.image.load("./data/images/bg.jpg"), (WIDTH_WINDOW, HEIGHT_WINDOW))
        # Theme setting
        font = pygame_menu.font.FONT_8BIT
        my_theme = pygame_menu.Theme(
            background_color=(0, 0, 0, 50),
            widget_background_color=(0, 255, 0, 50),
            widget_font_color=(255, 102, 255),
            widget_margin=(0, 10),
            widget_padding=10,
            widget_font=font,
            widget_font_size=24,
            title_font_size=24
        )

        self.menu = pygame_menu.Menu('Group 19 - K67EEI', 300, 300, theme=my_theme)
        self.menu.add.selector(
            "AI Depth: ", [(str(i), i) for i in range(1, 6)],
            onchange=self.set_depth
        )
        self.menu.add.button("Restart", self.restart)
        self.menu.add.button("Play", button_id='PvP')
        self.menu.add.button("Play with AI", button_id='PvC')
        self.menu.add.button("Quit", sys.exit, 1)

        self.running = True

    def set_depth(self, selected, value):
        # Ghi giá trị mới vào file settings.py
        with open("src/settings.py", "r") as file:
            lines = file.readlines()

        with open("src/settings.py", "w") as file:
            for line in lines:
                if line.strip().startswith("DEPTH ="):
                    file.write(f"DEPTH = {value}\n")
                else:
                    file.write(line)
    def restart(self):
        python = sys.executable
        os.execv(python, [python] + sys.argv)

    def mainLoop(self):
        while self.running:
            events = pygame.event.get()
            self.menu.update(events)
            self._draw_background()
            self.menu.draw(self.screen)
            pygame.display.update()

    def _draw_background(self):
        self.screen.blit(self.bg, (0, 0))