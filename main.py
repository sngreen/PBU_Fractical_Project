#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @package    
# @brief      
#
# @version    $Revision: $
# @author     Sergey Green
# @note       
# @note       $Date:     $
# @note       $URL:      $
#

import sys
import os
import yaml # type: ignore
import logging
from data_ops import csv_op, json_op, txt_op
from datetime_ops import datetime_op
from shell_ops import data_type
from format_ops import format_out
from argparse import ArgumentParser, HelpFormatter
from settings.settings import MENU_FILE, LOG_FILE, REPORT_FILE

logging.basicConfig(
    format = '%(asctime)s %(levelname)8s %(filename)10s:%(lineno)4s %(funcName)14s() | %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%SZ',
    level = logging.DEBUG,
    handlers = [
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(filename = LOG_FILE, mode = 'a'),
    ],
)

LOGGER = logging.getLogger(__name__)

FILE_FORMATS = {
    'application/json': 'json',
    'application/csv': 'csv',
    'text/csv': 'csv',
    'text/plain': 'txt',
    'inode/x-empty': 'any'
}

class PBUFinalProject:
    def __init__(self):
        self.get_menu()
        self.get_options()
        file_format: str = self.verify_infile()
        data: dict = self.get_data(file_format)
        data: dict = self.add_data(data)
        data: str = self.format_data(data)
        self.write_file(data)
 
    def get_menu(self) -> None:
        '''
        Read in menu (yaml) file. The content is used for menu.
        '''

        with open(MENU_FILE, 'r') as menu_input:
            setattr(self, 'menu_options', yaml.load(menu_input, Loader=yaml.FullLoader))

    def get_options(self) -> None:
        '''
        Display menu (with -h option)
        Collect input parameters
        '''
        
        parser: argparse.ArgumentParser = ArgumentParser(
            prog = os.path.basename(__file__),
            usage = '{} [arg] | -h'.format(os.path.basename(__file__)),
            formatter_class = lambda prog: HelpFormatter(prog, max_help_position=50))
        
        input_file: list = [('--{}'.format(arg.strip()),
            'required: %(required)s, default: %(default)s',
            dict(required=True, default=None, metavar='<{}>'.format(arg.strip())))
                for arg in self.menu_options['input_file'].split()]

        for args, desc, options in input_file:
            parser.add_argument(args, help=desc, **options)

        self.args: argparse.Namespace = parser.parse_args()

    def verify_infile(self) -> str:
        '''
        Verify the infile is valid;
            a. file exists
            b. file of the processable format

            if the input has no content:
                write the evidence to the output file and exit
            else:
                return the format name of the file

        Return:
            Name of the format.
        '''

        LOGGER.info('')

        if not os.path.isfile(self.args.file_name):
            LOGGER.debug(f'File "{self.args.file_name}" does not exist ..')
            sys.exit(1)

        file_format: str = data_type.get_file_type(self.args.file_name)

        if not file_format in FILE_FORMATS.keys():
            LOGGER.info(f'File "{self.args.file_name}" is of format "{file_format}", which is not supported by this application.')
            sys.exit(1)

        if os.stat(self.args.file_name).st_size == 0:
            self.write_file(f'---\nNo content to be analyzed in the file on {self.args.file_name}\n---\n')
            sys.exit(0)

        return FILE_FORMATS.get(file_format)

    def get_data(self, file_format: str) -> dict:

        '''
        Select which file to call for extracting data from a given file.

        Parameters:
            file_format (str): Valid format of the file.
        Returns:
            processed analysis from the extracted data
        '''

        LOGGER.info('')

        module: module = globals()[f'{file_format}_op']
        data: dict = getattr(module, 'get_data')(self.args.file_name)

        return getattr(module, 'show_count')(data)
        
    def get_timestamp(self) -> str:
        '''
        Get timestamp (when this script ran)
        '''

        LOGGER.info('')

        today: datetime.datetime = datetime_op.get_today()

        return datetime_op.datetime_str(today)
    
    def add_data(self, data: dict) -> dict:
        '''
        Add additional information to the collected from a file analysis

        Parameters:
            data (dict): processed analysis from the extracted data

        Returns:
            data (dict): full data needed for further formatting
        '''

        LOGGER.info('')

        additional_info: dict = {
            'file_name': self.args.file_name,
            'timestamp': self.get_timestamp()
        }
        return {**data, **additional_info}

    def format_data(self, data: dict) -> str:
        '''
        Formatted output from the auxiliary package
        '''

        return format_out.format_output(data)
    
    def write_file(self, data: str) -> None:
        '''
        Write data to a file

        Parameters:
            data (str): formatted clear text data
        '''

        fname: str = REPORT_FILE.replace('users', self.args.file_name.split(os.path.sep)[-1])
        with open(fname, 'w') as outfile:
            outfile.write(data)
            LOGGER.info(f'wrote: {fname}')

def main():
    PBUFinalProject()

if __name__ == '__main__':
    main()