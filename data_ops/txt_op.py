import re

def get_data(file_name: str) -> str:
    with open(file_name, 'r') as infile:
       return re.sub('[^a-z A-Z]', '', infile.read())

def show_count(data: str) -> dict:
    return {
        'word count': len(data.split())
    }
