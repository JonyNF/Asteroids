import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
       
    #set GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #groups to avoid complex code
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Shot.containers = (shots, updatable, drawable)
    
    dt = 0
    
    while True:
        #Close game process if screen closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update all updatable objects
        for obj in updatable:
            obj.update(dt)

        #fill screen with black color
        screen.fill((0,0,0))
        
        #draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
            
        for obj in asteroids:
            if obj.is_colliding(player):
                print("Game over!")
                return
        
        #Refresh the screen
        pygame.display.flip()
        
        #force game to render at a max 60 fps so cpu consume is not excessive
        dt = clock.tick(60)/ 1000
            
    
if __name__ == "__main__":
    main()
