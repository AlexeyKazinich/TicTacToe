import sys
import pygame
from square import Square

RENDER_SCALE = 2.0

class TicTacToe:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('TicTacToe')
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320,240))
        self.clock = pygame.time.Clock()
        self.player = "X"
        self.grid = {
            "0:0" : Square(self.screen,(0,0)),
            "0:1" :Square(self.screen, (0,1)),
            "0:2" :Square(self.screen, (0,2)),
            
            "1:0" :Square(self.screen,(1,0)),
            "1:1" :Square(self.screen,(1,1)),
            "1:2" :Square(self.screen,(1,2)),
            
            "2:0" :Square(self.screen,(2,0)),
            "2:1" :Square(self.screen,(2,1)),
            "2:2" :Square(self.screen,(2,2))
            
        }

    def draw_grid(self) -> None:
        '''draws the grid'''
        for key, value in self.grid.items():
            value.draw(self.screen)
        
        #draw lines
        for i in range(3):
            pygame.draw.line(self.screen,(0,0,0),(self.screen.get_width() / 3 * i,0), (self.screen.get_width() / 3 * i, self.screen.get_height()))
        for i in range(3):
            pygame.draw.line(self.screen,(0,0,0),(0,self.screen.get_height() / 3 * i),(self.screen.get_width(),self.screen.get_height() / 3 * i))
            

    def run(self) -> None:
        '''main gameloop, call this to run the game'''
        while True:
            self.display.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for key, value in self.grid.items():
                        if value.rect.collidepoint(pygame.mouse.get_pos()):
                            value.color = (0,255,0)
                            value.add_text(self.player)
                            if self.player == "X":
                                self.player = "O"
                            elif self.player == "O":
                                self.player = "X"
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                    
            
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()),(0,0))
            self.draw_grid()
            pygame.display.update()
            self.clock.tick(60)
    
TicTacToe().run()