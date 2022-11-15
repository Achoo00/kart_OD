import re
import numpy

#coord_stripped_grey = []
#coord_stripped_red = []
coords_grey = []
coords_red = []
labels_grey = []
labels_red = []
difference = []

#Coordinates: [tensor(202.), tensor(63.), tensor(947.), tensor(791.)]
#Label Name: orange 0.95
#Coordinates: [tensor(298.), tensor(1041.), tensor(868.), tensor(1754.)]
#Label Name: apple 0.95


def strip_grey(coord_1_grey):
    coord_stripped_grey = []
    for i in coord_1_grey:
        coord_2_grey = re.sub('\D', '', i)
        coord_stripped_grey.append(coord_2_grey)
    return coord_stripped_grey


def strip_red(coord_1_red):
    coord_stripped_red = []
    for i in coord_1_red:
        coord_2_red = re.sub('\D', '', i)
        coord_stripped_red.append(coord_2_red)
    return coord_stripped_red


while True:
    coord = input("coords")
    label = input("car colour")
    ok = coord.split()
    print(type(ok))
    if "grey" in label:
        coord = strip_grey(ok)
        print("coord", coord)
        labels_grey.append(label)
        coords_grey = coord
    elif "red" in label:
        coord = strip_red(ok)
        labels_red.append(label)
        coords_red = coord
    else:
        print("object not detected")

    test = [30, 300, 1200, 700]
    if len(coords_red) > 0 and len(coords_grey) > 0:
        diff = numpy.subtract(int(coords_grey[-1]), int(coords_red[-1]))  # [-1] for last element
        difference.append(diff)
        print("Difference:", difference[-1])
        if difference[-1] < 0:
            print("Grey in first")
        elif difference[-1] > 0:
            print("Red in first")
        elif difference[-1] == 0:
            print("Tied")
        else:
            print("Imaginary numbers")
    else:
        print("Not enough data")

    print("Grey coords:", coords_grey)
    print("Grey labels:", labels_grey)
    print("Red coords:", coords_red)
    print("Red labels:", labels_red)
