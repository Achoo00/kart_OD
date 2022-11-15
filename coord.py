import re
import numpy

x3 = []
coords_grey = []
coords_red = []
labels_grey = []
labels_red = []
difference = []

def strip(x1):
    for i in x1:
         x2 = re.sub('\D', '', i)
         #print(x2)
         x3.append(x2)

#x2 = re.sub('\D', '', str(xyxy))

xyxy1 = "[tensor(51.), tensor(180.), tensor(977.), tensor(589.)]" #car 1
#xyxy2 = "[tensor(30.), tensor(300.), tensor(1200.), tensor(700.)]" #car 2
ok = xyxy1.split()
#boomer = xyxy2.split()
strip(ok)
#strip(boomer)
print(x3)

while True:
    coord = input("coords")
    label = input("car colour")
    if "grey" in label:
        labels_grey.append(label)
        coords_grey.append(int(coord))
    elif "red" in label:
        labels_red.append(label)
        coords_red.append(int(coord))
    else:
        print("object not detected")

    #coord = "[tensor(51.), tensor(180.), tensor(977.), tensor(589.)]"  # car 1
    #label = "grey car"
    # = "[tensor(30.), tensor(300.), tensor(1200.), tensor(700.)]" #car 2
    #label2 = "red car"
    test = [30,300,1200,700]
    if len(coords_red) > 0 and len(coords_grey) > 0:
        #diff = numpy.subtract(coords_grey[-1],coords_red[-1]) # [-1] for last element
        diff = numpy.subtract(int(x3[1]), test[1])  # [-1] for last element
        difference.append(diff)
        print("Difference:",difference[-1])
        if difference[-1] > 0:
            print("Grey in first")
        elif difference[-1] < 0:
            print("Red in first")
        else:
            print("Imaginary numbers")
    else:
        print("Not enough data")

    print("Grey coords:",coords_grey)
    print("Grey labels:",labels_grey)
    print("Red coords:",coords_red)
    print("Red labels:",labels_red)






