# main.py

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
# Brief Description of what this module does. This module calls the functions from all other modules, and prints the decrypted messages and photo taken. 
# Citations: In-class material, Bill Nicholson, Copilot
# Anything else that's relevant: Everyone was involved in the making of this module. 
###############################################################################

from decryptionPackage.decryption import *
from photoPackage.photo import *
from txtPackage.txt import *
from jsonUtilitiesPackage.jsonUtilities import *
if __name__ == "__main__":
    
    printPhoto("./ProjectPhoto/BuildingAndMovieQuote.jpg")


    data = read_txt_to_list('./Data/UCEnglish.txt')
    indices = jsonValues()
    location = get_location(data, indices)

    location_str = ' '.join(location)

    print(location_str)

    data = jsonValuesForMovies()
    # The key given by Professor Nicholson
    key = b'WVRqW7wUIQ1mgbz5PAonHGJn-XknVdDV74L_RNFjU0o='

    # Decrypt the titles for "CompleteDuck"
    encrypted_titles = data["CompleteDuck"]
    decrypted_titles = [decrypt_movie_title(bytes(title, 'utf-8'), key) for title in encrypted_titles]

    for title in decrypted_titles:
        print(title)


