import pygame as py


# def is_mouse_over(rects: list[tuple[float, float, float, float]] | tuple[float, float, float, float]) -> bool:
#     mouse_x, mouse_y = py.mouse.get_pos()
#     if isinstance(rects, tuple):
#         rects = [rects]
#     return any(
#         rect[0] < mouse_x < rect[0] + rect[2] and rect[1] < mouse_y < rect[1] + rect[3]
#         for rect in rects
#     )

def is_mouse_over_list(rects: list[tuple[float, float, float, float]]) -> bool:
    mouse_x, mouse_y = py.mouse.get_pos()
    # Ensure rects is a list of valid tuples
    if isinstance(rects, tuple):
        rects = [rects]
    rects = [r for r in rects if isinstance(r, (tuple, list)) and len(r) == 4]
    return any(
        rect[0] < mouse_x < rect[0] + rect[2] and
        rect[1] < mouse_y < rect[1] + rect[3]
        for rect in rects
    )


def is_mouse_over(rect: tuple[float, float, float, float]) -> bool:
    """
    Function checking whether mouse cursor is hovering over specified rectangle.
    :param rect: Checked rectangle.
    :return: (bool) True if mouse is over specified rectangle or False otherwise.
    """
    mouse_x, mouse_y = py.mouse.get_pos()
    return (
            rect[0] < mouse_x < rect[0] + rect[2] and rect[1] < mouse_y < rect[1] + rect[3]
    )
