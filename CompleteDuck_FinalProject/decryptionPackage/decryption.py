# decryption.py

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
# Brief Description of what this module does. This module takes the encryption key given by the professor and defines a function that decypts the movie title using cryptography.ferent.
# Citations: In-class material, Bill Nicholson, Copilot
# Anything else that's relevant: Everyone was involved in the making of this module. 
###############################################################################

from cryptography.fernet import Fernet

def decrypt_movie_title(encrypted_title, key):
    """
    Decrypts an encrypted movie title using the provided key.
    @param encrypted_title bytes: The encrypted movie title.
    @param key bytes: The key used for decryption.
    @return str: The decrypted movie title.
    """
    # Initialize the Fernet object with the key
    fernet = Fernet(key)
    # Decrypt the title
    decrypted_title = fernet.decrypt(encrypted_title)
    # Convert bytes to string
    return decrypted_title.decode()
