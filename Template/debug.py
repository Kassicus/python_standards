# python module imports
import pygame

# project file imports
import lib

class DebugInterface:
    """
    overlay for displaying information, toggled by pressing [TAB]

    ...

    Attributes
    ----------
    active : bool
        determines if the interface is drawn
    offset : int
        universal offset from the right side of the screen
    font : pygame.Font
        font to render the interface with

    Methods
    -------
    get_fps(clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        creates a text object and an offset to render the fps
    get_mouse() -> list [pygame.Surface, int]:
        creates a text object and an offset to render the mouse position
    toggle_active():
        changes the active state of the interface
    draw():
        draws all of the interface objects at thier offsets
    """