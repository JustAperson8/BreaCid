import pygame


def download_image(name, colorkey=None):
    image = pygame.image.load(name)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image = image.convert()
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def download_map_format_brcd(name):
    """
    Brcd is an txt format
    :param name: path to file
    :return: lists
    """
    f = open(name, encoding="utf-8")
    data = []
    elem = []
    for i in f.readlines():
        if i[:3] == "###":
            data.append(elem)
            elem = []
        elif i.split()[0][:2] == "//":
            continue
        else:
            elem.append(list(map(int, i.rstrip('\n').split())))
    f.close()
    if is_correct_map(data):
        return data
    return data


def is_correct_map(data):
    cel = list(map(lambda x: len(x), data))
    return all(list(map(lambda y: y == cel[0], cel)))
