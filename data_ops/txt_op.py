import re

def get_data(file_name: str) -> str:
    '''
    Get data from text file
        Parameters:
            file_name (str): name of the file where data is to be taken from.
        Returns:
            clear text (content of the file)
    '''

    with open(file_name, 'r') as infile:
       return re.sub('[^a-z A-Z]', '', infile.read())

def show_count(data: str) -> dict:
    '''
    Get analysis from data
        Parameters:
            data (dict): dictionary of rows and columns 
        Returns:
            formatted dictionary of word counts
    '''

    return {
        'word count': len(data.split())
    }
