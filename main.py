from collections import deque
import pygame, time

pygame.init()

screen = pygame.display.set_mode([500, 500])

# 왼쪽 노트들
notes1 = deque([1, 3, 5, 7, 9])
now1 = deque()
# 오른쪽 노트들
notes2 = deque([2, 4, 6, 8, 10])
now2 = deque()

start_time = time.time()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    screen.fill((255, 192, 203))
    ### 여기에 배경 추가

    
    
    # 현재까지 지난 시간
    diff_time = time.time() - start_time
    
    # 현재 시간 ~ 2초 뒤 까지 보여주기
    while notes1 and notes1[0] <= diff_time+2:
        now1.append(notes1.popleft())
    while now1 and now1[0] <= diff_time:
        now1.popleft()
    
    while notes2 and notes2[0] <= diff_time+2:
        now2.append(notes2.popleft())
    while now2 and now2[0] <= diff_time:
        now2.popleft()
    
    for note in now1:
        height = (2 - (note - diff_time)) * 250
        pygame.draw.circle(screen, (255, 255, 255), (166, height), 10)
    for note in now2:
        height = (2 - (note - diff_time)) * 250
        pygame.draw.circle(screen, (255, 255, 255), (166*2, height), 10)

    pygame.display.flip()
