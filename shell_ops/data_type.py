import os
import subprocess

def get_file_type(file_name: str) -> str:
    '''
    Get the type of the file
    
    Parameters:
        file_name (str): Name of the file to examine
    Returns:
        Type of the file
    '''

    cmd = ["file", "{}".format(file_name), "--mime-type"]

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='unicode_escape', text=True)
    return result.stdout.split(':')[-1].strip()
