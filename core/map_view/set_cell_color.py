import os
from core.download_something.download_image import download_image

def set_cell_color(colors):
    """
    This function sets color or texture for cell
    :return: list of images and colors
    :param colors: list of colors or paths
    """
    lofcol = []
    for i in colors:
        if os.path.isfile(i):
            lofcol.append(download_image(i))
        else:
            lofcol.append(i)
    return lofcol