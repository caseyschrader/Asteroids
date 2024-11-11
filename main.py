import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import draw_score
import sys

pygame.font.init()
font = pygame.font.Font(None, 36)
score = 0

def draw_score(screen):
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10,10))


def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    global score
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    Player.containers = (drawable, updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        draw_score(screen)
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in updateable:
            sprite.update(dt)
        pygame.display.flip()
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid) == True:
                    asteroid.split()
                    shot.kill()
                    score += 1
                    
        clock.tick(60)
        



if __name__ == "__main__":
    main()

