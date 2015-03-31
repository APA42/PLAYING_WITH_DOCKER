# -*- coding: utf-8 -*-
import os
import psycopg2 as pg
from postgres_access import repositories


def create_bote_connection():
    return pg.connect(
        host=os.environ['COMPONENT_DB_HOST_ADDR'],
        port=os.environ['COMPONENT_DB_TCP_PORT'],
        database=os.environ['COMPONENT_DB_NAME'],
        user=os.environ['COMPONENT_DB_USER'],
        password=os.environ['COMPONENT_DB_PASSWORD']
    )


def create_APARepository():
    return repositories.APARepository(create_bote_connection())
