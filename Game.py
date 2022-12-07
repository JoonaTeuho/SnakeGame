import pygame
from snakeClass import Snake, screen_height, screen_width
from foodClass import Food, drawGrid

def main():
    pygame.init()

    # Ruudun ja pelin sisäisen kellon luonti
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    #Pelialueen luonti
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    # Madon ja Ruokakohteen luonti
    snake = Snake()
    food = Food()

    font = pygame.font.SysFont("impact",20)

    while (True):

        # Pelin alustaminen
        clock.tick(7)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()

        # Ruokakohteen syöminen
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = font.render("Score {0}".format(snake.score), 1, (0,0,0))
        high_score = font.render("High score {0}".format(snake.high_score), 1, (0,0,0))
        screen.blit(text, (5,10))
        screen.blit(high_score, (5,30))
        pygame.display.update()

main()