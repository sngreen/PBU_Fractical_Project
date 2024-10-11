import csv

def get_data(file_name: str) -> str:
    with open(file_name, newline='') as infile: 
       csv_reader = csv.DictReader(infile)
       return [row for row in csv_reader]

def show_count(data: dict) -> dict:
    rows = [row for row in data]
    return {
        'columns': len(rows[0].keys()),
        'rows': len(rows[0].keys())
        }