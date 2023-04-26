import pygame
from piece import Piece

COLOR_BLACK = 0, 0, 0
COLOR_WHITE = 255, 255, 255
COLOR_RED = 255, 0, 0
COLOR_GREEN = 0, 255, 0
COLOR_BLUE = 0, 0, 255


class Tetris:
    # move to settings
    window_size_w = 800
    window_size_h = 800
    field_height = 32
    field_width = 32
    block_height = window_size_h // field_height
    block_width = window_size_w // field_width
    speed = 7

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Tetris.window_size_w, Tetris.window_size_h))
        self.running = False
        self.pieces = []
        self.current_piece = Piece()

    def move_current_piece_right(self):
        self.current_piece.position_X += 1

    def move_current_piece_left(self):
        self.current_piece.position_X -= 1

    def move_current_piece_down(self):
        self.current_piece.position_Y += 1

    def render_piece(self, piece):
        for coords in piece.piece_coords:
            pygame.draw.rect(
                self.screen,
                COLOR_GREEN,
                (
                    (piece.position_X + coords[0]) * Tetris.block_width,
                    (piece.position_Y + coords[1]) * Tetris.block_height,
                    self.window_size_w // self.field_width,
                    self.window_size_h // self.field_height,
                )
            )

    def handle_piece(self):
        for coords in self.current_piece.piece_coords:
            self.render_piece(self.current_piece)
            if self.field_height - self.current_piece.position_Y <= 4:
                if (self.current_piece.position_Y + coords[1]) * Tetris.block_height >= self.window_size_h - Tetris.block_height:
                    self.pieces.append(self.current_piece)
                    self.current_piece = Piece()

    def fixed_update(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.screen.fill(COLOR_BLACK)
            for event in pygame.event.get():
                # KEYDOWN
                if event.type == pygame.KEYDOWN:
                    # ESCAPE
                    if event.dict.get('key') == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.QUIT:
                    running = False

            dt = clock.tick(Tetris.speed)
            self.draw_stable_pieces()
            self.handle_piece()
            self.move_current_piece_down()
            pygame.display.update()

    def draw_stable_pieces(self):
        for piece in self.pieces:
            self.render_piece(piece)

    def start(self):
        self.screen.fill(COLOR_BLACK)
        self.fixed_update()
        pygame.quit()
