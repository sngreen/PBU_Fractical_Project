import sys
import json

def get_data(file_name: str) -> dict:
    '''
    Get data from json file
        Parameters:
            file_name (str): name of the file where data is to be taken from.
        Returns:
            json object (with content of the loaded file).
    '''

    with open(file_name, 'r') as infile:
        return json.load(infile)

def show_count(data: dict) -> dict:
    '''
    Get analysis from data
        Parameters:
            data (dict): dictionary of rows and columns 
        Returns:
            formatted dictionary of root counts
    '''

    return {
        'root count': len([leaf for leaf in data])
    }
