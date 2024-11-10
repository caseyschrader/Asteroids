import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    Player.containers = (drawable, updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in updateable:
            sprite.update(dt)
        pygame.display.flip()
        clock.tick(60)
        



if __name__ == "__main__":
    main()

