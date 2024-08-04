import math
import argparse
parser = argparse.ArgumentParser(description='circle and dots')
parser.add_argument('file1', type=str)
parser.add_argument('file2', type=str)
args = parser.parse_args()
file1=args.file1
file2=args.file2
with open (file1) as file:
    data1 = file.read()
a, b, r = map(float, data1.split())


with open(file2)  as file:
    x, y = [], []
    for line in file:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))

num_points = len(x)
for i in range(num_points):
    d = math.sqrt((x[i]-a)**2+(y[i]-b)**2)
    if d == r:
        print ("0")
    elif d < r:
        print ("1")
    else:
        print ("2")
file.close()
