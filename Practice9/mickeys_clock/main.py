import pygame
import clock

pygame.init()

screen = pygame.display.set_mode((600, 600))

clock_bg = pygame.image.load("clock.jpeg")
hand = pygame.image.load("mickeyclock.jpeg")

clock_fps = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # фон (часы)
    screen.blit(clock_bg, (0, 0))

    # стрелки
    clock.draw(screen, hand, (200, 200))

    pygame.display.flip()
    clock_fps.tick(60)

pygame.quit()