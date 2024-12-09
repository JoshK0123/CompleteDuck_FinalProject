# jsonUtiltiies.py

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
# Brief Description of what this module does. This module reads json files and finds values from the json files. 
# Citations: In-class material, Bill Nicholson, Copilot
# Anything else that's relevant: Everyone was involved in the making of this module. 
###############################################################################


import json

def jsonValues():
    # Path to your JSON file
    file_path = './Data/EncryptedGroupHints Fall 2024 Section 001.json'

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Access the value associated with "CompleteDuck"
    complete_duck_values = data["CompleteDuck"]

    # Return the values
    return complete_duck_values

def read_txt_to_list(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def get_location(data, indices):
    return [data[int(i)].strip() for i in indices]  # Strip newline characters

def jsonValuesForMovies():
    # Path to your JSON file
    file_path = './Data/TeamsAndEncryptedMessagesForDistribution.json'

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Return the data
    return data



