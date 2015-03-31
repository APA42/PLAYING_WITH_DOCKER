# -*- coding: utf-8 -*-

from postgres_access import constants


class APARepository(object):

    def __init__(self, connection):
        self._connection = connection
        self._connection.autocommit = True

    def put(self, value):
        with self._connection.cursor() as cursor:
            cursor.execute("insert into {table_name} ({col2}) values ('{value}');".format(table_name=constants.TABLE_NAME,
                                                                                          col2=constants.TABLE_NAME_COL_2_NAME,
                                                                                          value=value))

    def find_all(self):
        with self._connection.cursor() as cursor:
            cursor.execute("select {col1},{col2} from {table_name};".format(col1=constants.TABLE_NAME_COL_1_NAME,
                                                                            col2=constants.TABLE_NAME_COL_2_NAME,
                                                                            table_name=constants.TABLE_NAME))
            return cursor.fetchall()

