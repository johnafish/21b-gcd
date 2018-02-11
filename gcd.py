from PIL import Image
from math import gcd

dim = 500 
data = []

img = Image.new('RGB', (dim, dim))

for i in range(1, dim+1):
    for x in range(1, dim+1):
        value = int(255 - (gcd(i,x)/dim) * 255.0)
        data.append((value, value, value))

img.putdata(data)
img.save("gcd.png")
