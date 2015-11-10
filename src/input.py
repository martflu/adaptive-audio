import pygame

class input:

    def __init__(self):        
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
        
    def update(self, logic, scene):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logic.exit_game("user clicked the close button")
            if hasattr(event, "key"):
                if event.type == 2:
                    if event.key == 27:
                        logic.exit_game("user pressed escape")
                    elif event.key == 273:
                        self.up = 1
                    elif event.key == 274:
                        self.down = 1 
                    elif event.key == 275:
                        self.right = 1
                    elif event.key == 276:
                        self.left = 1
                elif event.type == 3:
                    if event.key == 275:
                        self.right = 0
                    elif event.key == 276:
                        self.left = 0
                    elif event.key == 274:
                        self.down = 0    
                    elif event.key == 273:
                        self.up = 0              