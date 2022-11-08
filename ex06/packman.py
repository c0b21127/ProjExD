import pygame as pg
from pygame.locals import *
import sys
from random import randint

map = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0],
        [0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0],
        [0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0],
        [0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0],
        [0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2]]


SURFACE = Rect(0,0,320,320)


class Maze(pg.sprite.Sprite):
    def __init__(self,name,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(name).convert_alpha()
        self.image = pg.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.left = x * (self.rect.width)
        self.rect.top  = y * (self.rect.height)


    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Character(pg.sprite.Sprite):
    def __init__(self,name):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(name).convert_alpha()
        self.image = pg.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()

    
    def updata(self,char_x,char_y):
        self.rect.center = char_x
        self.rect.center = char_y


    def draw(self,surface):
        surface.blit(self.image,self.rect)
    


def main():
    row = col = 0
    x = y = 0
    pg.init()
    surface = pg.display.set_mode(SURFACE.size)
    blocks = pg.sprite.Group()
    for b1 in map:          
        for b2 in b1:       
            if   b2 == 0:
                blocks.add(Maze("fig/1.png", x, y))
            elif b2 == 1:
                blocks.add(Maze("fig/pg_bg.jpg", x, y))
            elif b2 == 2:
                blocks.add(Maze("fig/10.png", x, y))
            x += 1
    
        else:
            x = 0
            y += 1
    blocks.draw(surface)

    character = Character("fig/11.png")
    chra_x = int(40/2)
    char_y = int(40/2)


    while True:
        if map[row][col] != 2:
            blocks.draw(surface)
            character.update(char_x,char_y)
            character.draw(surface)

        else:
            font = pg.font.Font(None,20)
            text = font.render("GOAL",True,(224,224,255))

            surface.fill((0,0,0))
            surface.blit(text,[93,139])


        pg.display.update()
        pg.time.wait(20)
        for event in pg.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_LEFT:
                    if (char_x > 0      + 40) and (map[row][col-1] != 0):
                        col -= 1
                        char_x -= 40
                if event.key == K_RIGHT:
                    if (char_x < 320  - 40) and (map[row][col+1] != 0):
                        col += 1
                        char_x += 40
                if event.key == K_UP:
                    if (char_y > 0      + 40) and (map[row-1][col] != 0):
                        row -= 1
                        char_y -= 40
                if event.key == K_DOWN:
                    if (char_y < 320 - 40) and (map[row+1][col] != 0):
                        row += 1
                        char_y += 40
def exit():
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()       # ゲームの本体
