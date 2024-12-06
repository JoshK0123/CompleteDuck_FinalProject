# txt.py
from mainPackage.main import *

def read_txt_to_list(file_path):
    '''
    Read a txt file into a list.
    @return list: the list created from the file
    '''
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines]
