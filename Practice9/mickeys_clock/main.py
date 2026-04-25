import pygame
import clock

pygame.init()

screen = pygame.display.set_mode((900, 900))

clock_bg = pygame.image.load("clock.jpeg")
hand = pygame.image.load("mickeyclock.jpeg")

clock_fps = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # фон (часы)
    bg_rect = clock_bg.get_rect()
    bg_rect.center = (900 // 2, 900 // 2)
    screen.blit(clock_bg, bg_rect)

    # стрелки
    clock.draw(screen, hand, (900 // 2, 900 // 2))

    pygame.display.flip()
    clock_fps.tick(60)

pygame.quit()