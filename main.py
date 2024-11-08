import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 780
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 배경 이미지 로드 및 크기 조정
background = pygame.image.load("background.jpg")
background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# 슬라이더 설정
class Slider(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width, height):
        super().__init__()
        self.original_image = pygame.image.load(image_path)  # 슬라이더 이미지 로드
        self.image = pygame.transform.scale(self.original_image, (width, height))  # 이미지 크기 조정
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # 슬라이더 초기 위치 설정
        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.centery = pygame.mouse.get_pos()[1]
            # Y 좌표가 화면 범위를 벗어나지 않도록 제한
            self.rect.centery = max(self.min_y, min(self.max_y, self.rect.centery))

# 모든 슬라이더를 담을 그룹
slider_group = pygame.sprite.Group()

# 슬라이더 생성
num_sliders = 40
slider_spacing = 56

# 슬라이더 그룹 생성
group1_sliders = []
group2_sliders = []

for i in range(1, num_sliders + 1):
    if i <= num_sliders // 2:
        y = SCREEN_HEIGHT // 2 - 50
        group = group1_sliders
    else:
        y = SCREEN_HEIGHT - 50
        group = group2_sliders
    
    if i<=num_sliders//2:
        if(i <= 10):
            slider = Slider(i * slider_spacing, y, "slider.png", 50, 100)
    
        else:
            slider = Slider((i+1) * slider_spacing - 20, y, "slider.png", 50, 100)
    else:
        if(i <= 30):
            slider = Slider((i-20) * slider_spacing, y, "slider.png", 50, 100)
    
        else:
            slider = Slider((i-19) * slider_spacing - 20, y, "slider.png", 50, 100)

    group.append(slider)
    slider_group.add(slider)

# 그룹 별로 y축 제한 범위 설정
for slider in group1_sliders:
    slider.min_y = 80
    slider.max_y = SCREEN_HEIGHT // 2 - 50

for slider in group2_sliders:
    slider.min_y = SCREEN_HEIGHT // 2 + 80
    slider.max_y = SCREEN_HEIGHT - 50

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 시 슬라이더를 드래그할 수 있도록 설정
            for slider in slider_group:
                if slider.rect.collidepoint(event.pos):
                    slider.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # 마우스 버튼 떼면 슬라이더 드래그 중지
            for slider in slider_group:
                slider.dragging = False

    # 화면 그리기
    screen.blit(background, (0, 0))
    slider_group.update()
    slider_group.draw(screen)
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
