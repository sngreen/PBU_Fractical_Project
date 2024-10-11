import sys
import json

def get_data(file_name: str) -> dict:
    with open(file_name, 'r') as infile:
        return json.load(infile)

def show_count(data: dict) -> dict:
    return {
        'root count': len([leaf for leaf in data])
    }
