import csv

def get_data(file_name: str) -> list:
    with open(file_name, newline='') as infile: 
       csv_reader: csv.DictReader = csv.DictReader(infile)
       return [row for row in csv_reader]

def show_count(data: dict) -> dict:
    rows: list = [row for row in data]
    return {
        'columns': len(rows[0].keys()),
        'rows': len(rows[0].keys())
    }