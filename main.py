# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * #imports all of constants.py, not usually done, just the parts that are needed
from player import PlayerShape

def main():
    pygame.init()                                                           #initializes pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))         #setting window to variables in constants
    clock = pygame.time.Clock()        
    player = PlayerShape(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)                                     
    dt = 0
    


    while True:
        for event in pygame.event.get():                                    #beginning of game loop, will check if user has closed the window and exits loop
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill("black")
        player.draw(screen)        
                                                
        pygame.display.flip()                                               #refreshes the "black" screen at each loop

        dt = clock.tick(60) / 1000                                          #limits fps to 60 /1000 = to convert from ms to s. It will pause the game loop until 1/60th of a second has passed.

if __name__ == "__main__":                                                  #only runs main() if main.py is called directly
    main()