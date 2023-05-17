
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

s = [100, 200, 300, 400, 500]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    screen.fill((255, 192, 203))

    for c in s:
        pygame.draw.circle(screen, (255, 255, 255), (166, c), 10)
        pygame.draw.circle(screen, (255, 255, 255), (166*2, c), 10)

        pygame.draw.rect(screen, (255, 255, 255), [150, 400, 30, 5])

    pygame.display.flip()

    for i in range(len(s)):
        s[i] += 0.05
        if s[i] > 500:
            del s[i]
            s.append(0)
        

