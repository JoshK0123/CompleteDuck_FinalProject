#main.py

from decryptionPackage.decryption import *
from photoPackage.photo import *
from txtPackage.txt import *
if __name__ == "__main__":
    
    printPhoto("BuildingAndMovieQuote.jpg")
    
    data = read_txt_to_list('./Data/UCEnglish.txt')
    indices = [7480, 28894, 8018, 46342, 42061, 103568, 346, 13068, 23887, 21407]
    Location = [data[i] for i in indices]

    flattened_Location = []

    def flatten_and_convert_to_str(item):
        '''
        Converts a nested list into a single flat list, and converts elements to strings after flattening.
        @return list: the flattened list
        '''
        if isinstance(item, list):
            for sub_item in item:
                flatten_and_convert_to_str(sub_item)
        else:
            flattened_Location.append(str(item))

    for item in Location:
        flatten_and_convert_to_str(item)

    Location_string = ' '.join(flattened_Location)

    print(Location_string)

    decrypt_movie_title(b'gAAAAABnJ6xXc8WnJ2DxuUMI3yz9g4ZaGNGUd6TPU96o-rmP1YfrxSq387RxZtyEt2Hc1WNWXcsUaz5oWJGd_W7Gs6wNXMoDG7bnwSawyeXVmuNEP88HlA8=',b'WVRqW7wUIQ1mgbz5PAonHGJn-XknVdDV74L_RNFjU0o=')