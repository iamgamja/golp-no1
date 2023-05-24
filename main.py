WHITE = (255,255,255)
BLACK = (0, 0, 0)

LEVEL_HEIGHT = 500

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

from collections import deque
import pygame, time

pygame.init()

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
bg = pygame.image.load("bg.png")

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# 왼쪽 노트들
notes1 = deque([1, 3, 5, 7, 9])
now1 = deque()
# 오른쪽 노트들
notes2 = deque([2, 4, 6, 8, 10])
now2 = deque()

start_time = time.time()

# 게임 시작으로부터 지난 시간 반환
def gettime():
    return time.time() - start_time

# (실제 텍스트, 언제까지)
TEXT = ('', float('inf'))

def settext(text):
    global TEXT
    TEXT = (text, time.time() + 0.5) # 0.5초 후까지
    
def perfect():
    print('perfect')
    settext('perfect')

def early():
    print('early')
    settext('early')

def late():
    print('late')
    settext('late')
    
def miss():
    print('miss')
    settext('miss')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            # f: 102, j: 106
            if event.key == 102:
                # left
                if not now1:
                    miss()
                else:
                    note = now1.popleft()
                    nowtime = gettime()
                    if abs(note - nowtime) <= 0.3:
                        perfect()
                    elif note < nowtime:
                        late()
                    else:
                        early()
            elif event.key == 106:
                # left
                if not now2:
                    miss()
                else:
                    note = now2.popleft()
                    nowtime = gettime()
                    if abs(note - nowtime) <= 0.3:
                        perfect()
                    elif note < nowtime:
                        late()
                    else:
                        early()

    # 배경
    screen.fill((255, 192, 203))
    screen.blit(bg, (0, 0))

    # 텍스트
    if TEXT[1] > time.time():
        text_surface = my_font.render(TEXT[0], False, (0, 0, 0))
        screen.blit(text_surface, (WINDOW_WIDTH/2-50,0))

    # 현재까지 지난 시간
    diff_time = gettime()
    
    # 현재 시간 ~ 2초 뒤 까지 보여주기
    while notes1 and notes1[0] <= diff_time+2:
        now1.append(notes1.popleft())
    while now1 and (2 - (now1[0] - diff_time)) / 2 * LEVEL_HEIGHT > WINDOW_HEIGHT:
        now1.popleft()
        miss()
    
    while notes2 and notes2[0] <= diff_time+2:
        now2.append(notes2.popleft())
    while now2 and (2 - (now2[0] - diff_time)) / 2 * LEVEL_HEIGHT > WINDOW_HEIGHT:
        now2.popleft()
        miss()
    
    for note in now1:
        height = (2 - (note - diff_time)) / 2 * LEVEL_HEIGHT
        pygame.draw.circle(screen, BLACK, (WINDOW_WIDTH/3, height), 10)
    for note in now2:
        height = (2 - (note - diff_time)) / 2 * LEVEL_HEIGHT
        pygame.draw.circle(screen, BLACK, (WINDOW_WIDTH/3*2, height), 10)

    pygame.display.flip()
