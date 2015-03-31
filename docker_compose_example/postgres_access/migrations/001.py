#!/usr/bin/env python

from postgres_access import factory, constants

bote_connection = factory.create_bote_connection()
bote_connection.autocommit = True

with bote_connection.cursor() as cursor:
    cursor.execute("DROP TABLE IF EXISTS {table_name};".format(table_name=constants.TABLE_NAME))
    cursor.execute("CREATE TABLE {table_name} ({col1}, {col2});".format(table_name=constants.TABLE_NAME,
                                                                       col1=constants.TABLE_NAME_COL_1_SDL,
                                                                       col2=constants.TABLE_NAME_COL_2_SDL))

print "001 Migration Done"