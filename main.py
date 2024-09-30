import pygame
from constants import *
from player import Player


def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #set GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        #Close game process if screen closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        player.update(dt)
        
        #fill screen with black color
        screen.fill((0,0,0))
        #draw player
        player.draw(screen)
        #Refresh the screen
        pygame.display.flip()
        
        
        #force game to render at a max 60 fps so cpu consume is not excessive
        dt = clock.tick(60)/ 1000
        

        
    
    
if __name__ == "__main__":
    main()
