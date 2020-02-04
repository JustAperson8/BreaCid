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


def download_list_of_images_format_brcd(name):
    f = open(name)
    data = []
    elem = []
    for i in f.readlines():
        if i[:3] == "###":
            data.append(elem)
            elem = []
        elif i.split()[0][:2] == "//":
            continue
        else:
            elem += (i.rstrip().split())
    f.close()
    return data
