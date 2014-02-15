"""
Helpers to convert between EAGLE color definitions (which are integers into an
arbitrary array) and other real-world color spaces.
"""

# This table can be populated by viewing the 'Color' selection dialog in the
# EAGLE layers editor. The colors are zero-indexed starting from the top left.
eagle_to_rgb = [
    (255, 255, 255),  # white
    (75, 75, 165),    # dark blue/indigo
    (75, 165, 75),    # green
    (75, 165, 165),   # teal
    (165, 75, 75),    # dark red/burgundy
    (165, 75, 165),   # magneta/purple
    (165, 165, 75),   # puke
    (165, 165, 165),  # medium gray
    (230, 230, 230),  # light gray
    (75, 75, 255),    # blue
    (75, 255, 75),    # neon green
    (75, 255, 255),   # cyan/neon blue
    (255, 75, 75),    # bright red
    (255, 75, 255),   # neon pink
    (255, 255, 75),   # yellow
    (75, 75, 75),     # dark gray
]

default_color_rgb = (165, 165, 165)  # medium gray


def as_rgb(number):
    """
    Convert an EAGLE color index to a r, g, b tuple.
    """
    try:
        return eagle_to_rgb[number]
    except IndexError:
        return default_color_rgb


def as_css(number):
    """
    Convert an EAGLE color index to a CSS color string.
    """
    return 'rgb(%d, %d, %d)' % as_rgb(number)
