import pygame
from pygame.gfxdraw import circle


# VARIOUS VARIABLES
running = True
scr_width = 1000
scr_height = 500
c1 = (0, 0, 0)
drag_symbols = False
x_mov = False
o_mov = False
pxx, pyx = 0, 0
pxo, pyo = 0, 0

x2 = False
x3 = False
x4 = False
x5 = False

# Functions
def img_click(img_rect, drag, mov):
    """
    The function takes three arguments, image rectangle, and two boolean values (drag and movement)
    it checks if there is a collision between the rectangle and the mouse, if that´s the case, it positions
    the image at px and py and return the values, also returns the drag and movement values
    """
    px = 0
    py = 0

    # Used to change the condition of x and o from T to F and vice versa
    drag = not drag
    mov = not mov
    # Calculated the distance between the top left position of the rectangle and the mose click position
    mox, moy = event.pos
    px = img_rect.x - mox
    py = img_rect.y - moy

    return px, py, drag, mov


def img_movement(img_rect, px, py, drag, mov):
    """
    :param img_rect: image rectangle
    :param px: image position in x
    :param py: image position in Y
    :param drag: dragging (bool)
    :param mov: movement (bool)
    :return: new position of rectangle (x, y)
    """
    if drag and mov:
        # Ensure the image always move accordingly to the mouse click position
        mouse_px, mouse_py = event.pos
        img_rect.x = mouse_px + px
        img_rect.y = mouse_py + py

    return img_rect.x, img_rect.y


def insert_img(img, i_width, i_height, pos_x, pos_y, *args):
    nim = pygame.image.load(img).convert_alpha()
    nim = pygame.transform.scale(nim, (i_width, i_height))
    nim.set_colorkey(*args)
    img_rect = nim.get_rect(topleft=(pos_x, pos_y))
    return nim, img_rect


pygame.init()

# Create screen
main_screen = pygame.display.set_mode((scr_width, scr_height))

# IMAGES
scl_wall, wall_rect = insert_img("images/wall.jpg", scr_width, scr_height, 0, 0)
scl_brd_frame, brd_frame_rect = insert_img("images/board_frame.png", scr_width - 300, scr_height - 30,
                                           280, scr_height - 490)
scl_board, board_rect = insert_img("images/board.jpg", scr_width - 340, scr_height - 70, 300, 30)
scl_grid, grid_rect = insert_img("images/grid.png", 350, 350, 450, 50, c1)
scl_x, x_rect = insert_img("images/x.png", 120, 120,0, 10, c1)
scl_o, o_rect = insert_img("images/circle.png", 120, 120,120, 10, c1)

# Static images
scl_x2, x_rect2 = insert_img("images/x.png", 120, 120,450, 60, c1)
scl_x3, x_rect3 = insert_img("images/x.png", 120, 120,571, 60, c1)


while running:
    # Display images in screen
    main_screen.blit(scl_wall, wall_rect)
    main_screen.blit(scl_brd_frame, brd_frame_rect)
    main_screen.blit(scl_board, board_rect)
    main_screen.blit(scl_grid, grid_rect)
    main_screen.blit(scl_x, x_rect)
    main_screen.blit(scl_o, o_rect)

    # Mouse
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if x_rect.collidepoint(event.pos):
                pxx, pyx, drag_symbols, x_mov = img_click(x_rect, drag_symbols, x_mov)

            elif o_rect.collidepoint(event.pos):
                pxo, pyo, drag_symbols, o_mov = img_click(o_rect, drag_symbols, x_mov)

        elif event.type == pygame.MOUSEMOTION:
            if drag_symbols and x_mov:
                img_movement(x_rect, pxx, pyx, drag_symbols, x_mov)
            elif drag_symbols and o_mov:
                img_movement(o_rect, pxo, pyo, drag_symbols, o_mov)

        elif event.type == pygame.MOUSEBUTTONUP:
            drag_symbols = False
            x_mov, o_mov = False, False

            if 450 <= x_rect.x <= 570 and 50 <= x_rect.y <= 110:
                x_rect.x, x_rect.y = 0, 10
                x2 = True
            elif 571 <= x_rect.x <= 691:
                x_rect.x, x_rect.y = 0, 10
                x3 = True

    if x2:
        main_screen.blit(scl_x2, x_rect2)
    if x3:
        main_screen.blit(scl_x3, x_rect3)


    pygame.display.update()
