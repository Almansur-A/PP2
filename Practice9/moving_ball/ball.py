import pygame

x = 100
y = 100
radius = 25
speed = 20

def move(keys, width, height):
    global x, y
    if keys[pygame.K_UP] and y - speed - radius >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + speed + radius <= height:
        y += speed
    if keys[pygame.K_LEFT] and x - speed - radius >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + speed + radius <= width:
        x += speed

def draw(screen):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)