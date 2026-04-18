import pygame
import ball

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball.move(keys, 600, 400)
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()