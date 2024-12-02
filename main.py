import pygame

pygame.init()


# VARIOUS VARIABLES
finished_game = False
running = True
scr_width = 1000
scr_height = 500

c1_x, r1_x = 0, 0
c2_x, r2_x = 0, 0
c3_x, r3_x = 0, 0

c1_o, r1_o = 0, 0
c2_o, r2_o = 0, 0
c3_o, r3_o = 0, 0

#matrix = {"0":"n", "1":"n", "2":"n", "3":"n", "4":"n", "5":"n", "6":"n", "7":"n", "8":"n"}

drag_symbols = False
x_mov = False
o_mov = False

# used to set a limit in the numbers of figures drawn in the grid
x_counter = 0
o_counter = 0

# Variables for the original images
sym_size = (120, 120)
pxx, pyx = 0, 0
pxo, pyo = 0, 0
c1 = (0, 0, 0)  # Removes bg colour from x and circle

# Variables related to the creation and position of image copies
top_lim = 50
left_col = 450
mid_col = 565
mid_top = 160
right_col = 685
bot_top = 285

# Variables used to draw and evaluate the existence of new images
x2, x2_rect, x2_check = None, None, False
x3, x3_rect, x3_check = None, None, False
x4, x4_rect, x4_check = None, None, False
x5, x5_rect, x5_check = None, None, False
x6, x6_rect, x6_check = None, None, False
x7, x7_rect, x7_check = None, None, False
x8, x8_rect, x8_check = None, None, False
x9, x9_rect, x9_check = None, None, False
x10, x10_rect, x10_check = None, None, False

o2, o2_rect, o2_check = None, None, False
o3, o3_rect, o3_check = None, None, False
o4, o4_rect, o4_check = None, None, False
o5, o5_rect, o5_check = None, None, False
o6, o6_rect, o6_check = None, None, False
o7, o7_rect, o7_check = None, None, False
o8, o8_rect, o8_check = None, None, False
o9, o9_rect, o9_check = None, None, False
o10, o10_rect, o10_check = None, None, False

# Functions
def img_click(img_rect, drag, mov):
    """
    The function takes three arguments, image rectangle, and two boolean values (drag and movement)
    it checks if there is a collision between the rectangle and the mouse, if that´s the case, it positions
    the image at px and py and return the values, also returns the drag and movement values
    """

    # Used to change the condition of x and o from T to F and vice versa
    drag = not drag
    mov = not mov
    # Calculated the distance between the top left position of the rectangle and the mose click position
    mox, moy = event.pos
    px = img_rect.x - mox
    py = img_rect.y - moy

    return px, py, drag, mov


def img_movement(img_rect, px, py, drag, mov):
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


def copy_images(img, pos_x, pos_y):
    img2 = img.copy()
    img2_rect = img2.get_rect(topleft=(pos_x, pos_y))
    return img2, img2_rect


# Create screen
main_screen = pygame.display.set_mode((scr_width, scr_height))

# IMAGES
scl_wall, wall_rect = insert_img("images/wall.jpg", scr_width, scr_height, 0, 0)
scl_brd_frame, brd_frame_rect = insert_img("images/board_frame.png", scr_width - 300, scr_height - 30,
                                           280, scr_height - 490)
scl_board, board_rect = insert_img("images/board.jpg", scr_width - 340, scr_height - 70, 300, 30)
scl_grid, grid_rect = insert_img("images/grid.png", 350, 350, 450, 50, c1)
scl_x, x_rect = insert_img("images/x.png", sym_size[0], sym_size[1],0, 10, c1)
scl_o, o_rect = insert_img("images/circle.png",sym_size[0], sym_size[1],120, 10, c1)

while running:
    # Display images in screen
    main_screen.blit(scl_wall, wall_rect)
    main_screen.blit(scl_brd_frame, brd_frame_rect)
    main_screen.blit(scl_board, board_rect)
    main_screen.blit(scl_grid, grid_rect)
    main_screen.blit(scl_x, x_rect)
    main_screen.blit(scl_o, o_rect)

    # Display Xs
    if x2_check:
        main_screen.blit(x2, x2_rect)
    if x3_check:
        main_screen.blit(x3, x3_rect)
    if x4_check:
        main_screen.blit(x4, x4_rect)
    if x5_check:
        main_screen.blit(x5, x5_rect)
    if x6_check:
        main_screen.blit(x6, x6_rect)
    if x7_check:
        main_screen.blit(x7, x7_rect)
    if x8_check:
        main_screen.blit(x8, x8_rect)
    if x9_check:
        main_screen.blit(x9, x9_rect)
    if x10_check:
        main_screen.blit(x10, x10_rect)

    # Display Os
    if o2_check:
        main_screen.blit(o2, o2_rect)
    if o3_check:
        main_screen.blit(o3, o3_rect)
    if o4_check:
        main_screen.blit(o4, o4_rect)
    if o5_check:
        main_screen.blit(o5, o5_rect)
    if o6_check:
        main_screen.blit(o6, o6_rect)
    if o7_check:
        main_screen.blit(o7, o7_rect)
    if o8_check:
        main_screen.blit(o8, o8_rect)
    if o9_check:
        main_screen.blit(o9, o9_rect)
    if o10_check:
        main_screen.blit(o10, o10_rect)

    # Resolutions to draw line when winning:

    # Columns references
    if c1_x == 3 or c1_o == 3:
        vl_1, vl1_rect = insert_img("images/vcl_line.png", 100, 360, left_col + 20, 50, c1)
        main_screen.blit(vl_1, vl1_rect)
        finished_game = True

    elif c2_x == 3 or c2_o == 3:
        vl_1, vl1_rect = insert_img("images/vcl_line.png", 100, 360, mid_col + 20, 50, c1)
        main_screen.blit(vl_1, vl1_rect)
        finished_game = True

    elif c3_x == 3 or c3_o == 3:
        vl_1, vl1_rect = insert_img("images/vcl_line.png", 100, 360, right_col + 20, 50, c1)
        main_screen.blit(vl_1, vl1_rect)
        finished_game = True

    # Rows references
    if r1_x == 3 or r1_o == 3:
        hz_1, hz_1_rect = insert_img("images/hztl_line.png", 360, 120, left_col, top_lim, c1)
        main_screen.blit(hz_1, hz_1_rect)
        finished_game = True

    elif r2_x == 3 or r2_o == 3:
        hz_1, hz_1_rect = insert_img("images/hztl_line.png", 360, 120, left_col, mid_top, c1)
        main_screen.blit(hz_1, hz_1_rect)
        finished_game = True

    elif r3_x == 3 or r3_o == 3:
        hz_1, hz_1_rect = insert_img("images/hztl_line.png", 360, 120, left_col, bot_top, c1)
        main_screen.blit(hz_1, hz_1_rect)
        finished_game = True

    # Mouse
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if x_rect.collidepoint(event.pos):
                pxx, pyx, drag_symbols, x_mov = img_click(x_rect, drag_symbols, x_mov)

            elif o_rect.collidepoint(event.pos):
                pxo, pyo, drag_symbols, o_mov = img_click(o_rect, drag_symbols, x_mov)

        # With this section we ensure that the game is still on, so we can move figures as long as finished game is false
        if not finished_game:
            if event.type == pygame.MOUSEMOTION:
                if drag_symbols and x_mov:
                    img_movement(x_rect, pxx, pyx, drag_symbols, x_mov)
                elif drag_symbols and o_mov:
                    img_movement(o_rect, pxo, pyo, drag_symbols, o_mov)

            elif event.type == pygame.MOUSEBUTTONUP:
                drag_symbols = False
                x_mov, o_mov = False, False
                # In this section We check where X is positioned and depending on that where it´ll be located

                if x_counter < 5: # Limits the amount of Xs we can use
                    # First column
                    if left_col <= x_rect.x + sym_size[0]/2 <= (left_col + 110):
                        if top_lim <= x_rect.y + sym_size[1]/2 <= 145 and x2_check == False and o2_check == False:
                            x2, x2_rect = copy_images(scl_x, left_col, top_lim)
                            x2_check = True  # so we can blit the image
                            x_counter += 1
                            r1_x += 1

                        elif 160 < x_rect.y + sym_size[1]/2 <= 280 and x3_check == False and o3_check == False:
                            x3, x3_rect = copy_images(scl_x, left_col, mid_top)
                            x3_check = True
                            x_counter += 1
                            r2_x += 1

                        elif 285 < x_rect.y + sym_size[1]/2 <= 390 and x4_check == False and o4_check == False:
                            x4, x4_rect = copy_images(scl_x, left_col, bot_top )
                            x4_check = True
                            x_counter += 1
                            r3_x += 1

                        c1_x += 1

                    # Second column
                    elif mid_col < x_rect.x + sym_size[0]/2 <= right_col:
                        if top_lim < x_rect.y + sym_size[1]/2 <= mid_top and x5_check == False and o5_check == False:
                            x5, x5_rect = copy_images(scl_x, mid_col, top_lim)
                            x5_check = True
                            x_counter += 1
                            r1_x += 1

                        elif mid_top < x_rect.y + sym_size[1]/2 <= bot_top and x6_check == False and o6_check == False:
                            x6, x6_rect = copy_images(scl_x, mid_col, mid_top)
                            x6_check = True
                            x_counter += 1
                            r2_x += 1

                        elif bot_top < x_rect.y + sym_size[1]/2 <= bot_top + 120 and x7_check == False and o7_check == False:
                            x7, x7_rect = copy_images(scl_x, mid_col, bot_top)
                            x7_check = True
                            x_counter += 1
                            r3_x += 1

                        c2_x += 1

                    # Third column
                    elif right_col < x_rect.x + sym_size[0]/2 <= right_col + 110:
                        if top_lim < x_rect.y + sym_size[1]/2 <= mid_top and x8_check == False and o8_check == False:
                            x8, x8_rect = copy_images(scl_x, right_col, top_lim)
                            x8_check = True
                            x_counter += 1
                            r1_x += 1

                        elif mid_top < x_rect.y + sym_size[1]/2 <= bot_top and x9_check == False and o9_check == False:
                            x9, x9_rect = copy_images(scl_x, right_col, mid_top)
                            x9_check = True
                            x_counter += 1
                            r2_x += 1

                        elif bot_top < x_rect.y + sym_size[1]/2 <= bot_top + 120 and x10_check == False and o10_check == False:
                            x10, x10_rect = copy_images(scl_x, right_col, bot_top)
                            x10_check = True
                            x_counter += 1
                            r3_x += 1

                        c3_x += 1

                    x_rect.x, x_rect.y = 0, 10  # return the original image to its start position
                else:
                    x_rect.x, x_rect.y = 0, 10  # return the original image to its start position

                # Os Section
                if o_counter < 5: # Limits the amount of Os we can use
                    # First column
                    if left_col <= o_rect.x + sym_size[0]/2 <= (left_col + 110):
                        if top_lim <= o_rect.y + sym_size[1]/2 <= 145 and o2_check == False and x2_check == False:
                            o2, o2_rect = copy_images(scl_o, left_col, top_lim)
                            o2_check = True  # so we can blit the image
                            o_counter += 1
                            r1_o += 1

                        elif 160 < o_rect.y + sym_size[1]/2 <= 280 and o3_check == False and x3_check == False:
                            o3, o3_rect = copy_images(scl_o, left_col, mid_top)
                            o3_check = True
                            o_counter += 1
                            r2_o += 1

                        elif 285 < o_rect.y + sym_size[1]/2 <= 390 and o4_check == False and x4_check == False:
                            o4, o4_rect = copy_images(scl_o, left_col, bot_top )
                            o4_check = True
                            o_counter += 1
                            r3_o += 1

                        c1_o += 1

                    # Second column
                    elif mid_col < o_rect.x + sym_size[0]/2 <= right_col:
                        if top_lim < o_rect.y + sym_size[1]/2 <= mid_top and o5_check == False and x5_check == False:
                            o5, o5_rect = copy_images(scl_o, mid_col, top_lim)
                            o5_check = True
                            o_counter += 1
                            r1_o += 1

                        elif mid_top < o_rect.y + sym_size[1]/2 <= bot_top and o6_check == False and x6_check == False:
                            o6, o6_rect = copy_images(scl_o, mid_col, mid_top)
                            o6_check = True
                            o_counter += 1
                            r2_o += 1

                        elif bot_top < o_rect.y + sym_size[1]/2 <= bot_top + 120 and o7_check == False and x7_check == False:
                            o7, o7_rect = copy_images(scl_o, mid_col, bot_top)
                            o7_check = True
                            o_counter += 1
                            r3_o += 1

                        c2_o += 1

                    # Third column
                    elif right_col < o_rect.x + sym_size[0]/2 <= right_col + 110:
                        if top_lim < o_rect.y + sym_size[1]/2 <= mid_top and o8_check == False and x8_check == False:
                            o8, o8_rect = copy_images(scl_o, right_col, top_lim)
                            o8_check = True
                            o_counter += 1
                            r1_o += 1

                        elif mid_top < o_rect.y + sym_size[1]/2 <= bot_top and o9_check == False and x9_check == False:
                            o9, o9_rect = copy_images(scl_o, right_col, mid_top)
                            o9_check = True
                            o_counter += 1
                            r2_o += 1

                        elif bot_top < o_rect.y + sym_size[1]/2 <= bot_top + 120 and o10_check == False and x10_check == False:
                            o10, o10_rect = copy_images(scl_o, right_col, bot_top)
                            o10_check = True
                            o_counter += 1
                            r3_o += 1

                        c3_o += 1

                    o_rect.x, o_rect.y = 120, 10  # return the original image to its start position
                else:
                    o_rect.x, o_rect.y = 120, 10  # return the original image to its start position

        else:
            pass
    pygame.display.update()
