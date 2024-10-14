from shell_ops import data_type

format = '{:<28}: {}'

def format_output(data: dict) -> tuple:
    '''
    Format output.

    Parameters:
        data (dict): data dictionary
    Returns:
        formatted 3-line string output
    '''

    first_line = format.format('File Name', data.get('file_name'))
    file_format: str = data_type.get_file_type(data.get('file_name'))

    if file_format in 'text/csv application/csv'.split():
        rows_columns = '{} rows, {} columns'.format(data.get('rows'), data.get('columns'))
        second_line = format.format('Number of Rows And Columns', rows_columns)
    elif file_format == 'text/plain':
        second_line = format.format('Number of Words', data.get('word count'))
    elif file_format == 'application/json':
        second_line = format.format('Root Count', data.get('root count'))

    third_line = format.format('Analysis Performed At', data.get('timestamp'))

    return tuple_str((first_line, second_line, third_line))

def tuple_str(tup):
    '''
    Convert tuple to string.

    Parameters:
        tup (tuple): 3 lines of text
    Returns:
        formatted string
    '''

    str_out = ''
    for item in tup:
        str_out = str_out + item + '\n'
    return str_out