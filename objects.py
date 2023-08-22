#imports
import pygame as pg


class Rectangle:
    def __init__(self,x,y,width,height,window)-> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = pg.Color(255,255,255)
        self.__rect = pg.Rect(x,y,width,height)
        self.window = window
    
    def set_color(self,R,G,B)-> None:
        self.color = pg.Color(R,G,B)

    def set_color(self,color: str)-> None:
        self.color = pg.Color(str(color))

    def draw(self)-> None:
        pg.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height))
    
    def draw_box(self)-> None:
        pg.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height),2)

    def collidepoint(self,locations) -> bool:
        self.__rect = pg.Rect(self.x,self.y,self.width,self.height)
        if(self.__rect.collidepoint(locations)):
            return True
        else:
            return False

class Button:
    def __init__(self,x,y,width,height,text,window, centered_x = False)-> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        
        if centered_x:
            self.center_of_screen_x()
            
        self.text = text
        self.color = pg.Color('lightskyblue3')
        self.textColor = pg.Color('lightskyblue3')
        self.hoverColor = pg.Color('deepskyblue1')
        self.font = pg.font.Font(None,32)
        self.__rectangle = Rectangle(self.x,self.y,self.width,self.height,window)
        self.__rectangle.set_color('lightskyblue3')
        

        #mouse events
        self.pressed = False
        self.confirmed = False
        self.hover = False
        
        


    #checks if the button was pressed, sets the value to false to prevent the button from staying pressed
    def get_pressed(self)-> None:
        temp = self.pressed
        self.pressed = False
        return temp
    
    def center_of_screen_x(self):
        self.x = (self.window.get_width() / 2) - (self.width / 2)
        
    def set_active(self)-> None:
        self.color = pg.Color('dodgerblue2')
        self.textColor = pg.Color('dodgerblue2')
        self.__rectangle.set_color('dodgerblue2')

    def set_deactive(self)-> None:
        self.color = pg.Color('lightskyblue3')
        self.textColor = pg.Color('lightskyblue3')
        self.__rectangle.set_color('lightskyblue3')
    
    def set_hover(self)-> None:
        self.color = self.hoverColor
        self.textColor = self.hoverColor
        self.__rectangle.set_color('deepskyblue1')

    def set_color(self,color)-> None:
        self.color = pg.Color(color)
        self.textColor = pg.Color(color)


    def collidepoint(self,locations) -> bool:
        if(self.__rectangle.collidepoint(locations)):
            return True
        else:
            return False

    def draw(self)-> None:

        #render the current font
        self.textRender = self.font.render(self.text,True,self.textColor)

        #draw the outline
        self.__rectangle.draw_box()

        #draw the text
        self.window.blit(self.textRender,(self.x+5,self.y+5))

        #check if hovering or clicking the button
        self.check_click()
    
    def check_click(self)-> None:
        mouse_pos = pg.mouse.get_pos() #mouse pos
        #if hovering
        if self.__rectangle.collidepoint(mouse_pos):
            self.hover = True
            self.set_hover()
        else: 
            self.hover = False
            self.set_deactive()
            
        #if clicking while hovering
        if(self.hover):
            if(pg.mouse.get_pressed()[0]):
                self.set_active()
                self.pressed = True
            else: self.pressed = False

