
import pygame
import sys

from const import *


class Main:


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def mainloop(self):
        pass




if __name__ == "__main__":
    main = Main()
    main.mainloop()