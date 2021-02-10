import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper (AbstractContextManager, ABC):

    def __init__(self):
        self._connection = None

    def __enter__(self):

        if os.getenv('GAE_ENV', '').startswith('standard'):
            self._connection = connector.connect(user='root', password='OENLztvvKm4fuen3', unix_socket='/cloudsql/electionsystem-hdm:europe-west3:electionsystem-hdm', database='electionsystem_hdm')
        else:
            self._connection = connector.connect(user='web357_35', password='XfJbuWNoVCpdnx5l', host='s217.goserver.host', database='web357_db35')
        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def insert(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, object):
        pass

    