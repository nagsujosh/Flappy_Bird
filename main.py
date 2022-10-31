import random
import time

import pygame
from pygame.locals import *

fps = 120
clock = pygame.time.Clock()

pygame.display.set_caption("Flappy Bird")

class Game:

    screen_size = (1000, 700)
    screen = pygame.display.set_mode(screen_size)
    background = None
    background_rect = None
    player_y = 60
    player_x = 60
    pipes = None
    pipes_rect = None
    pipe_obstacle = None
    pipe_obstacle_rect = None
    obstacle_height = None
    rand_num = None
    text = None
    font = None
    textpos = None
    bird = None
    bird_rect = None
    over = False

    def initialise(self):

        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)

    def _background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load("background.png")
        self.background = self.background.convert()
        self.background = pygame.transform.scale(self.background, self.screen_size)
        self.background_rect = self.background.get_rect()

    def obstacle(self):
        self.obstacle_width = 60
        self.obstacle_start_pos = 1700


        self.bot_obstacle_length = random.randint(0, 550)
        self.bot_obstacle = pygame.Surface((self.obstacle_width, self.bot_obstacle_length))
        self.bot_obstacle_rect = self.bot_obstacle.fill(
            (0, 0, 0))
        self.bot_obstacle_rect.x = self.obstacle_start_pos
        self.bot_obstacle_rect.y = 700 - self.bot_obstacle_length

        self.top_obstacle_length = abs(700 - 150 - self.bot_obstacle_length)
        self.top_obstacle = pygame.Surface((self.obstacle_width, self.top_obstacle_length))
        self.top_obstacle_rect = self.top_obstacle.fill((0, 0, 0))  # pygame.Surface.get_rect(self.top_obstacle)
        self.top_obstacle_rect.x = self.obstacle_start_pos
        self.top_obstacle_rect.y = 0

        self.obstacle_rect_list = [self.top_obstacle_rect, self.bot_obstacle_rect]
        self.obstacle_list = [self.top_obstacle, self.bot_obstacle]

    def obstacle_pos_update(self):
        self.top_obstacle_rect.x = self.obstacle_start_pos
        self.bot_obstacle_rect.x = self.obstacle_start_pos

    def player(self):
        self.bird = pygame.image.load("dove.png")
        self.bird = pygame.transform.flip(self.bird, True, False)
        self.bird = pygame.transform.scale(self.bird, (self.player_x, self.player_y))
        self.bird_rect = self.bird.get_rect()
        self.bird_rect.x = 60
        self.bird_rect.y = 60


class Blit(Game):
    def blitting(self):
        game_one.initialise()
        game_one._background()
        game_one.screen.blit(game_one.background, game_one.screen_size)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            key = pygame.key.get_pressed()
            if key[K_SPACE] and game_one.bird_rect.y < 690:
                if game_one.bird_rect.y > 0:
                    game_one.bird_rect.y -= 4

            elif game_one.bird_rect.y < 695:
                if not key[K_SPACE]:
                    game_one.bird_rect.y += 3

            game_one.obstacle_start_pos -= 4
            if game_one.obstacle_start_pos < -10:
                game_one.obstacle()
            game_one.obstacle_pos_update()

            game_one.screen.blit(game_one.background, game_one.background_rect)
            game_one.screen.blit(game_one.bird, game_one.bird_rect)
            game_one.screen.blit(game_one.top_obstacle, game_one.top_obstacle_rect)
            game_one.screen.blit(game_one.bot_obstacle, game_one.bot_obstacle_rect)
            pygame.display.flip()
            clock.tick(fps)

            if game_one.bird_rect.y >= 694 or game_one.bot_obstacle_rect.colliderect(
                    game_one.bird_rect) or game_one.top_obstacle_rect.colliderect(game_one.bird_rect):
                game_one.over = True
                game_one.game_over = pygame.font.Font(None, 100).render("Game Over!", 1, (255, 0, 0))
                game_one.game_over_pos = game_one.game_over.get_rect()
                game_one.game_over_pos.centerx = game_one.background.get_rect().centerx
                game_one.game_over_pos.centery = game_one.background.get_rect().centery
                game_one.screen.blit(game_one.game_over, game_one.game_over_pos)
                pygame.display.flip()

            if game_one.over == True:
                time.sleep(3)


game_one = Game()
should_blit = Blit()


def main():
    game_one.initialise()
    game_one._background()
    game_one.obstacle()
    game_one.player()
    should_blit.blitting()


if __name__ == '__main__':
    main()    
