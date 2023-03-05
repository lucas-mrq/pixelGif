from PIL import Image

# Open the source image
im = Image.open('PixelArt.png')

# Load the pixels of the source image
pixelMap = im.load()

# Define a list of reference colors
tab = [(143, 149, 163, 255), (109, 137, 177, 255), (188, 168, 143, 255), (110, 96, 83, 255), 
       (50, 52, 49, 255), (104, 86, 82, 255), (231, 231, 231, 255), (25, 25, 25, 255), 
       (101, 166, 188, 255), (192, 159, 141, 255), (0, 120, 208, 255), (0, 35, 100, 255), 
       (240, 40, 45, 255), (0, 166, 81, 255)]

# Define a function to calculate the distance between two colors
def distance(color1, color2):
    return ((color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2)**0.5

# Create a new image with the same size as the source image
newImg = Image.new(im.mode, im.size)

# Load the pixels of the new image
newPixelMap = newImg.load()

# Loop through all the pixels of the source image
for i in range(im.size[0]):
    for j in range(im.size[1]):
        # Find the closest reference color
        colorIndex = 0
        for k in range(1, len(tab)):
            if distance(pixelMap[i, j], tab[k]) < distance(pixelMap[i, j], tab[colorIndex]):
                colorIndex = k
        # Assign the corresponding reference color to the pixel of the new image
        newPixelMap[i, j] = tab[colorIndex]

# Close the source image
im.close()

# Display the converted image
newImg.show()

# Save the converted image
newImg.save("out.png")

# Close the converted image
newImg.close()
