import pygame

pygame.init()

run = True
m_sc = pygame.display.set_mode((500, 500))
x = pygame.image.load("images/x.png").convert_alpha()
x = pygame.transform.scale(x, (100, 100))
x.set_colorkey((0, 0, 0))
xr = x.get_rect(topleft=(10, 10))
dra = False
xmo = False
p_x = 0
p_y = 0

def im_cl(fr, dr, fm):
    """
    The function takes three arguments, image rectangle, and two boolean values (drag and movement)
    it checks if there is a collision between the rectangle and the mouse, if that´s the case, it positions
    the image at px and py and return the values, also returns the drag and movement values
    """
    px = 0
    py = 0

    if fr.collidepoint(event.pos):
        # Used to change the condition of x and o from T to F and vice versa
        dr = not dr
        fm = not fm
        # Calculated the distance between the top left position of the rectangle and the mose click position
        mox, moy = event.pos
        px = fr.x - mox
        py = fr.y - moy

    return px, py, dr, fm


def im_mv(fr, px, py, dr, fm):
    """
    :param fr: image rectangle
    :param px: image position in x
    :param py: image position in Y
    :param dr: dragging (bool)
    :param fm: movement (bool)
    :return:
    """
    if dr and fm:
        # Ensure the image always move accordingly to the mouse click position
        mouse_px, mouse_py = event.pos
        fr.x = mouse_px + px
        fr.y = mouse_py + py

    return fr.x, fr.y


while run:
    m_sc.fill((145, 120, 200))
    m_sc.blit(x, xr)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            p_x, p_y, dra, xmo = im_cl(xr, dra, xmo)

        elif event.type == pygame.MOUSEMOTION:
            if dra and xmo:
                im_mv(xr, p_x, p_y, dra, xmo)

        elif event.type == pygame.MOUSEBUTTONUP:
            dra = False
            xmo = False

    pygame.display.update()




