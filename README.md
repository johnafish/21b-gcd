# 21b-gcd
A cool GCD problem for Harvard Math 21B [hw06](http://sites.fas.harvard.edu/~math21b/handouts/hw06.pdf) 5c!

I wanted to explore the pattern shown in the image with the GCD(x,y) corresponding to pixel intensity:

![The Pattern](https://github.com/johnafish/21b-gcd/blob/master/gcd.png)

And found (not surprisingly) that the lines drawn correspond to the relationship by=ax for integral (a,b) with pixel intensities (x/b or y/a). Realizing this allowed me to draw a simulation of the GCD image for a,b in [1,10]:

![Simulated Image](https://github.com/johnafish/21b-gcd/blob/master/line_intensity.png)

Which looks really similar! It is not, of course, the same image, but the relationship holds true as [a,b] -> [y,x] (which would then just be a linear way of solving GCD, which isn't very efficient considering the efficiency of the Euclidean algorithm).
