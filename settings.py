# coding: utf-8
import os
import sys
import logging

BASEDIR = os.path.dirname(__file__)

CONFIG = {
    'template_path': os.path.join(BASEDIR, 'templates'),
    'static_path': os.path.join(BASEDIR, 'static'),
    'debug': False
}

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)8s %(name)s - %(message)s',
    datefmt='%H:%M:%S'
)
