import pygame
class Square:
    def __init__(self, screen: pygame.display, coords : tuple):
        print(list(coords))
        self.coords = list(coords)
        self.screen = screen
        self._text = None
        self.color = (255,255,255)
        self.rect = pygame.Rect(((screen.get_width() * self.coords[0] /3),(screen.get_height() * self.coords[1] /3)), #location
                                (screen.get_width() / 3,screen.get_height()/ 3)) #size
        
    @property
    def text(self) -> None:
        return self._text
    
    @text.setter
    def text(self, text: str) -> None:
        self._text = text
        
    def reset(self) -> None:
        self._text = None
    
    def draw(self, screen : pygame.display) -> None:
        """draw the square, and the text if it has one"""
        pygame.draw.rect(screen,self.color,self.rect)
        
        
        if self.text is not None:
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_new = my_font.render(self.text,False,(0,0,0))
            self.screen.blit(text_new,(self.rect.centerx - (text_new.get_width() / 2), self.rect.centery - (text_new.get_height()/2)))
    