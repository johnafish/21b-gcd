from PIL import Image
from math import gcd

dim = 500
data = []

img = Image.new('RGB', (dim, dim))
data = []
values = list(range(1,11)) 

def line_value(i,x):
    for a in values:
        for b in values:
            if a*i == b*x:
                return (0,0,0)
    return (255,255,255)

for i in range(1, dim+1):
    for x in range(1, dim+1):
        data.append(line_value(i,x))

img.putdata(data)
img.save("line.png")
