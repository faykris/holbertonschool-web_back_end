#!/usr/bin/env python3
"""0. Regex-ing"""
from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format - return filtered values with a format"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter_datum - returns log message obfuscated"""
    for field in fields:
        message = re.sub(r'(?<={}=)[^{}]+'.format(field, separator),
                         redaction, message)
    return message


def get_logger() -> logging.Logger:
    """get_logger - return logger object"""
    logging = logging.getLogger('user_data')
    logging.setLevel(logging.INFO)
    logging.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logging.addHandler(handler)
    return logging


def get_db() -> mysql.connector.connection.MySQLConnection:
    """get_db - return mysql database connector"""
    connector = mysql.connector.connect(
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME')
    )
    return connector
