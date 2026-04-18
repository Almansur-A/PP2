import pygame
import player

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
font = pygame.font.Font(None, 36)

running = True

while running:
    screen.fill((0, 0, 0))

    text = font.render(f"Track: {player.playlist[player.current]}", True, (255,255,255))
    screen.blit(text, (50, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            if event.key == pygame.K_s:
                player.stop()
            if event.key == pygame.K_n:
                player.next_track()
            if event.key == pygame.K_b:
                player.prev_track()
            if event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()