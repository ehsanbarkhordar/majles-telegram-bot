#!/usr/bin/env python
import configparser
import os
import logging

config = configparser.ConfigParser()
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './config.ini')
config.read(filename)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
