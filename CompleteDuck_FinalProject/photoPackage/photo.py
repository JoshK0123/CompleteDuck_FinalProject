#Photo.py


from PIL import Image

def printPhoto(image_path):

# Path to the image file
    image_path = "BuildingAndMovieQuote.jpg"

# Load the image
    image = Image.open(image_path)

# Display the image
    image.show()
