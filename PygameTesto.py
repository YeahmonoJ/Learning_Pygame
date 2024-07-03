import pygame, sys

class Game:
    """
    FUTURE NOTES:
    HIGHER LEFT VALUE means to the right 
    LOWER LEFT VALUE means to the left
      """
    def __init__(self) -> None:
#Creates game window and Title"""
        pygame.init()
        self.COLOR = (43,43,43)
        self.SCREEN_X_AND_Y = (1080, 720)
        pygame.display.set_caption("TESTO!!")
        self.SCREEN = pygame.display.set_mode(self.SCREEN_X_AND_Y)
        
#BUTTONS, Button Colors, Main Menu"""
#QUIT BUTTON 
        self.BUTTON_TEXT_COLOR_QUIT = 'white'
        self.BUTTON_COLOR_QUIT = (200,200,200)
        self.BUTTON_COLOR_HIGHLIGHTED_QUIT = (43,43,43)
        self.BUTTON_FONT_QUIT = pygame.font.SysFont('Times New Roman', 75, bold=True)
        self.BUTTON_SURFACE_QUIT = self.BUTTON_FONT_QUIT.render("QUIT", True, self.BUTTON_COLOR_QUIT)
        self.BUTTON_QUIT = pygame.Rect(880, 460, 200,200)

# OPTIONS BUTTON 
        self.BUTTON_TEXT_COLOR_OPTIONS = 'white'
        self.BUTTON_COLOR_OPTIONS = (200,200,200)
        self.BUTTON_COLOR_HIGHLIGHTED_OPTIONS = (43,43,43)
        self.BUTTON_FONT_OPTIONS = pygame.font.SysFont('Times New Roman', 50, bold=True)
        self.BUTTON_SURFACE_OPTIONS = self.BUTTON_FONT_OPTIONS.render("OPTIONS", True, self.BUTTON_COLOR_OPTIONS)
        self.BUTTON_OPTIONS = pygame.Rect(850, 350, 200,200)




    def Game_Window(self):
        self.SCREEN.fill(self.COLOR)

#Button Collision Detection
        a,b = pygame.mouse.get_pos()
        
        if self.BUTTON_OPTIONS.x <= a <= self.BUTTON_OPTIONS.x + 250 and self.BUTTON_OPTIONS.y <= b <= self.BUTTON_OPTIONS.y + 75:
            pygame.draw.rect(self.SCREEN, (self.BUTTON_COLOR_HIGHLIGHTED_OPTIONS), self.BUTTON_OPTIONS)
            self.BUTTON_SURFACE_OPTIONS = self.BUTTON_FONT_OPTIONS.render("OPTIONS", True, self.BUTTON_TEXT_COLOR_OPTIONS)
            
        else:
            pygame.draw.rect(self.SCREEN, (self.BUTTON_COLOR_HIGHLIGHTED_OPTIONS), self.BUTTON_OPTIONS)
            self.BUTTON_SURFACE_OPTIONS = self.BUTTON_FONT_OPTIONS.render("OPTIONS", True, self.BUTTON_COLOR_OPTIONS)
            
        self.SCREEN.blit(self.BUTTON_SURFACE_OPTIONS,(self.BUTTON_OPTIONS.x + 5, self.BUTTON_OPTIONS.y + 5))

#
        if self.BUTTON_QUIT.x <= a <= self.BUTTON_QUIT.x + 200 and self.BUTTON_QUIT.y <= b <= self.BUTTON_QUIT.y + 85:
            pygame.draw.rect(self.SCREEN, (self.BUTTON_COLOR_HIGHLIGHTED_QUIT), self.BUTTON_QUIT)
            self.BUTTON_SURFACE_QUIT = self.BUTTON_FONT_QUIT.render("QUIT", True, self.BUTTON_TEXT_COLOR_QUIT)
               
        else:
            pygame.draw.rect(self.SCREEN, (self.BUTTON_COLOR_HIGHLIGHTED_QUIT), self.BUTTON_QUIT)
            self.BUTTON_SURFACE_QUIT = self.BUTTON_FONT_QUIT.render("QUIT", True, self.BUTTON_COLOR_QUIT)
            
        self.SCREEN.blit(self.BUTTON_SURFACE_QUIT,(self.BUTTON_QUIT.x + 5, self.BUTTON_QUIT.y + 5))
        

        pygame.display.update()
    
    def Game_Exit(self):

# Closes game if the X button is clicked on the window

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

# Closes game if the user hits the ESC key

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Checks if Mouse cursor is CLICKED ON THE  QUIT button         
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.BUTTON_QUIT.collidepoint(event.pos):

                    pygame.quit()
                    sys.exit()
        

def main():
    game = Game()
    GAME_IS_RUNNING = True

    while GAME_IS_RUNNING:
        game.Game_Window()
        game.Game_Exit()



        pygame.display.flip()



if __name__=='__main__':
    main()