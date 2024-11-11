import pygame

pygame.font.init()
font = pygame.font.Font(None, 36)
global score

def draw_score(screen):
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10,10))
