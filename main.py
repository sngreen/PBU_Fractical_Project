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
import magic
import logging
from data_ops import csv_op, json_op, txt_op
from datetime_ops import datetime_op
from format_ops import jinja_format
from argparse import ArgumentParser, HelpFormatter
from settings.settings import MENU_FILE, LOG_FILE, REPORT_FILE

logging.basicConfig(
    format="%(asctime)s %(levelname)8s %(filename)10s:%(lineno)4s %(funcName)14s() | %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(filename=LOG_FILE, mode="w"),
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
        file_format = self.verify_infile()
        data = self.get_data(file_format)
        data = self.add_data(data)
        data = self.format_data(data)
        self.write_file(data)
 
    def get_menu(self) -> None:
        '''
        Axiliary to local get_options() method. 
        Read in menu definition (yaml) file into local menu_options variable.
        '''
        with open(MENU_FILE, 'r') as menu_input:
            setattr(self, 'menu_options', yaml.load(menu_input, Loader=yaml.FullLoader))

    def get_options(self) -> None:
        '''
        Create dynamic menu (arg) variable from local menu_options parameter.
        '''
        parser = ArgumentParser(
            prog = os.path.basename(__file__),
            usage = '{} [arg] | -h'.format(os.path.basename(__file__)),
            formatter_class = lambda prog: HelpFormatter(prog, max_help_position=50))

        input_file = [('--{}'.format(arg.strip()),
            'required: %(required)s, default: %(default)s',
            dict(required=True, default=None, metavar='<{}>'.format(arg.strip())))
                for arg in self.menu_options['input_file'].split()]
        
        for args, desc, options in input_file:
            parser.add_argument(args, help=desc, **options)

        self.args = parser.parse_args()

    def verify_infile(self) -> str:
        '''
        Verify input file;
            a. file exists
            b. file of the format defined by the extension
            c. file is empty (send empty message to the output)

            Parameters:
                    None

            Returns:
                    File extension: str
        '''
        LOGGER.info('')

        if not os.path.isfile(self.args.file_name):
            LOGGER.debug(f'File "{self.args.file_name}" does not exist ..')
            sys.exit(1)

        file_format = magic.from_file(self.args.file_name, mime = True)
        if not file_format in FILE_FORMATS.keys():
            LOGGER.info(f'File "{self.args.file_name}" is of format "{file_format}", which is not supported by this application.')
            sys.exit(1)

        if os.stat(self.args.file_name).st_size == 0:
            self.write_file(f'---\nNo content to be analyzed in the file on {self.args.file_name}\n---\n')
            sys.exit(0)

        return FILE_FORMATS.get(file_format)

    def get_data(self, file_format: str) -> dict:
        '''
        Read in (through axiliary methods) data from a given file.
        
            Parameters:
                    file extension: str

            Returns:
                    data: dict
        '''
        LOGGER.info('')
        module = globals()[f'{file_format}_op']
        data = getattr(module, 'get_data')(self.args.file_name)
        return getattr(module, 'show_count')(data)
        
    def get_timestamp(self) -> str:
        '''
        Get timestamp
        
            Parameters:
                    None

            Returns:
                    timestamp: str
        '''
        LOGGER.info('')
        today = datetime_op.get_today()
        return datetime_op.datetime_str(today)
    
    def add_data(self, data: dict) -> dict:
        '''
        Add name of the input file, datestamp to the collected data.
        
            Parameters:
                    data: dict

            Returns:
                    data: dict
        '''
        LOGGER.info('')
        additional_info = {
            'file_name': self.args.file_name,
            'timestamp': self.get_timestamp()
        }
        return {**data, **additional_info}
        
    def format_data(self, data: dict) -> str:
        '''
        Format output (through jinja2)
        
            Parameters:
                    data: str

            Returns:
                    data: str
        '''
        LOGGER.info('')
        return jinja_format.render_template(
            os.path.join(os.getcwd(),'templates', 'template.j2'),
            data=data )

    def write_file(self, data: str) -> None:
        '''
        Write formatted output into a file.
        
            Parameters:
                    data: str
        '''
        fname = REPORT_FILE.replace('users', self.args.file_name.split(os.path.sep)[-1])
        with open(fname, 'w') as outfile:
            outfile.write(data)
            LOGGER.info(f'wrote: {fname}')

def main():
    PBUFinalProject()

if __name__ == '__main__':
    main()