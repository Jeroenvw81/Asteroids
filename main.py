# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * #imports all of constants.py, not usually done, just the parts that are needed
from player import PlayerShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    pygame.init()                                                           #initializes pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))         #setting window to variables in constants
    clock = pygame.time.Clock()        
                                       
    dt = 0

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)


    PlayerShape.containers = (updatable, drawable)

    player = PlayerShape(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  

    while True:
        for event in pygame.event.get():                                    #beginning of game loop, will check if user has closed the window and exits loop
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)                                                #update game state

        for asteroid in asteroids:
            if asteroid.collides_with(player):                              #calls the collides_with function to check for collision
                print("Game over!")
                sys.exit()
                

        screen.fill("black")                                                #clear screen  
        
        for entity in drawable:                                             #draw the entities
            entity.draw(screen)     
        
        pygame.display.flip()                                               #show the new frame

        dt = clock.tick(60) / 1000                                          #limits fps to 60 /1000 = to convert from ms to s. it calculates the new delta time

if __name__ == "__main__":                                                  #only runs main() if main.py is called directly
    main()