import pygame
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode([500, 500])

def start_drawing(body):
    screen.fill((255, 255, 255))

    time = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        magnitudes = body.get_magnitudes(time)

        pygame.draw.circle(screen, (0, 0, 255), (time, int((SCREEN_WIDTH / 2) - magnitudes[0])), 5)
        pygame.draw.circle(screen, (0, 255, 0), (time, int((SCREEN_WIDTH / 2) - magnitudes[1])), 5)
        pygame.draw.circle(screen, (255, 0, 0), (time, int((SCREEN_WIDTH / 2) - magnitudes[2])), 5)
        
        time += 1

        pygame.display.flip()

    pygame.quit()