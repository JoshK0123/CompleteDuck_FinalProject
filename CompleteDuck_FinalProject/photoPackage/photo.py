# photo.py

###############################################################################
# Name: Kazuhide Watnabe, Alex Patton, Alex Carnes, Joshu Klingelhafer
# email:  watanake@mail.uc.edu
#         pattona6@mail.uc.edu
#         carnesas@mail.uc.edu
#         klingejh@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 12/10/24
# Course #/Section: IS4010/001
# Semester/Year: Fall/2024
# Brief Description of the assignment: This assignment required the group to decode encrypted messages in two different ways, one requiring the encryption key, and the other using indexing.
#                                      Then we needed to take a photo to show in the results of the solution.
# Brief Description of what this module does. This module defines a function that gives the path to the image file, loads, and displays the photo our group took at the location that was decrypted. 
# Citations: In-class material, Bill Nicholson, Copilot
# Anything else that's relevant: Everyone was involved in the making of this module. 
###############################################################################


from PIL import Image

def printPhoto(image_path):

# Path to the image file
    image_path = "./ProjectPhoto/BuildingAndMovieQuote.jpg"

# Load the image
    image = Image.open(image_path)

# Display the image
    image.show()
