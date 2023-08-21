import pygame
class Square:
    def __init__(self, screen, coords : tuple):
        print(list(coords))
        self.coords = list(coords)
        self.screen = screen
        self.color = (255,255,255)
        screen_size = screen.get_size()
        self.rect = pygame.Rect(((screen.get_width() * self.coords[0] /3),(screen.get_height() * self.coords[1] /3)), #location
                                (screen.get_width() / 3,screen.get_height()/ 3)) #size
    
    
    def draw(self, surface) -> None:
        pygame.draw.rect(surface,self.color,self.rect)
        
    
    def add_text(self) -> None:
          pass  
    