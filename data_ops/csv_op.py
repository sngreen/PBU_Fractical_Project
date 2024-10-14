import csv

def get_data(file_name: str) -> list:
    '''
    Get data from csv file
        Parameters:
            file_name (str): name of the file where data is to be taken from.
        Returns:
            list of rows
    '''

    with open(file_name, newline='') as infile: 
       csv_reader: csv.DictReader = csv.DictReader(infile)
       return [row for row in csv_reader]

def show_count(data: dict) -> dict:
    '''
    Get analysis from data
        Parameters:
            data (dict): dictionary of rows and columns 
        Returns:
            formatted dictionary of counts (columns, rows)
    '''

    rows: list = [row for row in data]

    return {
        'columns': len(rows[0].keys()),
        'rows': len(rows)
    }