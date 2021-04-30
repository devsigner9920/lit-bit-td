# library import
import configparser
import sys
import os

# module import
from server import database
from modules import market

if __name__ == '__main__':
    ABS_PATH = sys.path[0] + os.sep

    # config file reader
    config = configparser.ConfigParser()
    config.read('app.cfg')

    # db connection
    db_info = config['db_info']
    db = database.db()

    market.get_market()
