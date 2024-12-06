# txt.py

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
# Brief Description of what this module does. This module defines a function that will take the txt file given by the professor to convert into a list in order to use for indexing.
# Citations: In-class material, Bill Nicholson
# Anything else that's relevant: Everyone was involved in the making of this module. 
###############################################################################

from mainPackage.main import *

def read_txt_to_list(file_path):
    '''
    Read a txt file into a list.
    @return list: the list created from the file
    '''
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines]
