import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Screen Blinking and Rotation Effect")

colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]

def display_rainbow_color(color):
    screen.fill(color)
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    
    angle = 0
    rotating = False
    center = (width // 2, height // 2)

    color_index = 0
    color_switch_time = 300  
    last_color_change = pygame.time.get_ticks()

    start_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = pygame.time.get_ticks()
        if current_time - last_color_change > color_switch_time:
            color_index = (color_index + 1) % len(colors)
            last_color_change = current_time
        
        display_rainbow_color(colors[color_index])

        if current_time > start_time + 2000:
            rotating = True
        
        if rotating:
            angle += 1
            if angle >= 360:
                angle = 0

            rotated_surface = pygame.Surface((width, height), pygame.SRCALPHA)
            rotated_surface.fill((0, 0, 0, 0))
            rotated_surface.blit(screen, (0, 0))

            rotated_image = pygame.transform.rotate(rotated_surface, angle)
            rotated_rect = rotated_image.get_rect(center=center)
            screen.fill((0, 0, 0))
            screen.blit(rotated_image, rotated_rect.topleft)

            pygame.display.flip()

        if current_time > start_time + 60000:
            screen.fill((139, 0, 0))
            font = pygame.font.Font(None, 100)
            text = font.render("thanks for the bitcoins))))", True, (255, 255, 255))
            text_rect = text.get_rect(center=(width // 2, height // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

        clock.tick(60)

if __name__ == "__main__":
    main()
