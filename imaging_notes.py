import Image

image_file = Image.open('0027.jpg')

# Convert to black and white
image_file = image_file.convert('1')

# Save
image_file.save('bw.jpg')

# Convert to black and white, setting a better threshold
# 15 may work as a value.
image2 = image_file.point(lambda p: p > 20 and 255).convert('1')

# View the image
image2.show()

# Create a histogram (count each pixel in the 0-255 range).
hist = image2.histogram()

# hist:
# [885227,
# 0,
# 0,
# ...
# 0,
# 0,
# 533]

# Black 
hist[0]

# White
hist[255]

num_pixels = sum(hist)

#In [110]: num_pixels
#Out[110]: 885760

if (100 * float(hist2[0]) / float(num_pixels)) > 99: 
     print "Discard"
     
# Discard

