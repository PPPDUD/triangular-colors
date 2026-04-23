from itertools import product
from tqdm import tqdm
from json import dumps

all_colors = product(list(range(1, 256)), list(range(1, 256)), list(range(1, 256)))
triangular_colors = []
acute_colors = []
obtuse_colors = []
right_colors = []


def type_of_color(color: tuple):
    if color[0] ** 2 + color[1] ** 2 > color[2] ** 2:
        return "acute"
    elif color[0] ** 2 + color[1] ** 2 == color[2] ** 2:
        return "right"
    elif color[0] ** 2 + color[1] ** 2 < color[2] ** 2:
        return "obtuse"


for i in tqdm(all_colors):
    ordered = i
    if ordered[0] + ordered[1] > ordered[2]:
        color_type = type_of_color(ordered)
        triangular_colors.append([i, color_type[0]])

        if color_type == "acute":
            acute_colors.append(i)
        elif color_type == "obtuse":
            obtuse_colors.append(i)
        elif color_type == "right":
            right_colors.append(i)


f = open("colors.json", "w")
f.write(dumps(triangular_colors))
f.close()

f = open("pythagorean.json", "w")
f.write(dumps(right_colors))
f.close()

f = open("acute.json", "w")
f.write(dumps(acute_colors))
f.close()

f = open("obtuse.json", "w")
f.write(dumps(obtuse_colors))
f.close()
