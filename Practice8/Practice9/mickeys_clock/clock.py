import pygame
import datetime

def draw(screen, hand_img, center):
    now = datetime.datetime.now()

    sec = now.second + now.microsecond / 1000000
    minute = now.minute + sec / 60

    sec_angle = -6 * sec
    min_angle = -6 * minute 
    sec_hand = pygame.transform.rotate(hand_img, sec_angle)
    min_hand = pygame.transform.rotate(hand_img, min_angle)

    sec_rect = sec_hand.get_rect(center=center)
    min_rect = min_hand.get_rect(center=center)

    # рисуем
    screen.blit(sec_hand, sec_rect)
    screen.blit(min_hand, min_rect)