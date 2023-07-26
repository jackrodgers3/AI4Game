import pygame
from random import randint
import math as m

TIME_LIMIT = int(input("How much time to collect candy? "))

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Simple collect game")
clock = pygame.time.Clock()
running = True
dt = 0


counter, text = TIME_LIMIT, f"Time left: {TIME_LIMIT}".rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
score = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
PLAYER_SIZE = 30
CANDY_SIZE = 30

candy_pos = pygame.Vector2(randint(CANDY_SIZE, screen.get_width()), randint(CANDY_SIZE, screen.get_height()))

while running:

    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = f"Time left: {counter}".rjust(3) if counter > 0 else 'done'
            if text == 'done':
                running = False
        if event.type == pygame.QUIT:
            running = False

    dist = m.sqrt(m.pow((player_pos.x - candy_pos.x), 2) + m.pow((player_pos.y - candy_pos.y), 2))
    min_length = PLAYER_SIZE + CANDY_SIZE
    if dist <= min_length:
        score += 1
        candy_pos = pygame.Vector2(randint(10, screen.get_width()), randint(10, screen.get_height()))
        counter += 10


    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, PLAYER_SIZE)

    pygame.draw.circle(screen, (160, 219, 179), candy_pos, CANDY_SIZE)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    screen.blit(font.render(text, 1, "black"), (32, 48))
    screen.blit(font.render(f"Score: {score}", 1, "black"), (732, 48))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

