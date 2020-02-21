from core.download_something.format_brcd import download_map_format_brcd


def save_map_format_brcd(file, data, titles):
    f = open(file, "w", encoding="UTF-8")
    f.write("""// This's just comment
// You must write date in this format:
// data
// title
// data1
// title1
// ...
// ### is just splitter, text after these symbols doesn't matter\n""")
    for i in range(len(data)):

        f.write(f"\n### {titles[i]}\n")
    f.close()


map_data = download_map_format_brcd("../../.data/maps/Test_map/h.brcd")
save_map_format_brcd("/home/daniil/h.brcd", map_data, ["cell_texture", "level_of_terrain", "texture_for_place"])
