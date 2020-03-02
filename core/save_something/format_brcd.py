def save_map_format_brcd(file, data, titles):
    f = open(file, "w", encoding="UTF-8")
    f.write("""// This's map data
// You must write date in this format:
// data
// title
// data1
// title1
// ...
// ### is just splitter, text after these symbols doesn't matter\n""")
    for i in range(len(data)):
        f.write('\n'.join([' '.join([str(x) for x in j]) for j in data[i]]))
        f.write(f"\n### {titles[i]}\n")
    f.close()


def save_list_of_images_format_brcd(file, data, titles):
    f = open(file, "w", encoding="UTF-8")
    f.write("// This's list of paths to textures or names of colors\n")
    for i in range(len(data)):
        f.write(' '.join(data[i]))
        f.write(f"\n### {titles[i]}\n")
    f.close()
