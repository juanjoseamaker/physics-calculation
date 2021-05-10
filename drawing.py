import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def start_drawing(body):
    screen.fill((255, 255, 255))

    time = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        magnitudes = body.get_magnitudes(time)  # (position, velocity, acceleration)

        # Print magnitudes

        pygame.draw.circle(screen, (0, 0, 255), (time, int((SCREEN_HEIGHT / 2) - magnitudes[0])), 3)
        pygame.draw.circle(screen, (0, 255, 0), (time, int((SCREEN_HEIGHT / 2) - magnitudes[1])), 3)
        pygame.draw.circle(screen, (255, 0, 0), (time, int((SCREEN_HEIGHT / 2) - magnitudes[2])), 3)

        # Print edge lines

        pygame.draw.circle(screen, (0, 0, 0), (time, int(SCREEN_HEIGHT / 2)), 2)

        if int(magnitudes[1]) == 0:
            pygame.draw.line(screen, (0, 0, 0), (time, 0), (time, SCREEN_HEIGHT), 2)
        
        time += 1

        pygame.display.flip()

    pygame.quit()