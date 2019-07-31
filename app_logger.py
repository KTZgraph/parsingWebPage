#coding=utf-8
#jeżeli jestem na linuch to dodaje sysloga

import couchdb
import platform
import logging

if platform.system() == 'Windows':
    print("latam na Windzie")
if platform.system() == 'Linux':
    print("cisne na Linux")
    import syslog

class AppLogger:
    def __init__(self,logger_name, logging_level = "INFO"):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel = getattr(logging, logging_level.upper()) #ustawianie poziomu logowania błedów
        self.file_handler = logging.FileHandler(logger_name.split('.')[0].lower() + '.log') #nazwa pliku z logiem ma sie konczyć log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler .setFormatter(formatter)
    
