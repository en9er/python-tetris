import pygame
from piece import Piece

COLOR_BLACK = 0, 0, 0
COLOR_WHITE = 255, 255, 255
COLOR_RED = 255, 0, 0
COLOR_GREEN = 0, 255, 0
COLOR_BLUE = 0, 0, 255


class Tetris:
    # move to settings
    window_size_w = 400
    window_size_h = 700
    block_size = window_size_w / 10

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Tetris.window_size_w, Tetris.window_size_h))
        self.running = False
        self.pieces = []
        self.current_piece = Piece()

    def draw_piece(self):
        piece_coords = self.current_piece.get_relative_coordinates()
        for coords in piece_coords:
            pygame.draw.rect(
                self.screen,
                COLOR_GREEN,
                (
                    coords[0] * Tetris.block_size,
                    coords[1] * Tetris.block_size,
                    Tetris.block_size,
                    Tetris.block_size
                )
            )

    def update(self):
        running = True
        while running:
            for event in pygame.event.get():
                # KEYDOWN
                if event.type == pygame.KEYDOWN:
                    # ESCAPE
                    if event.dict.get('key') == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.QUIT:
                    running = False

            self.draw_piece()
            pygame.display.update()

    def start(self):
        self.screen.fill(COLOR_BLACK)
        self.update()
        pygame.quit()
