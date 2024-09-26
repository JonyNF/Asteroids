import pygame
from constants import *


def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        screen.fill((0,0,0))
        
        #Close game process if screen closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        
        
        clock.tick(60) 
        dt = clock.tick()/60
        

        
    
    
if __name__ == "__main__":
    main()
