# -*- coding: utf-8 -*-

from peewee import *

settings = {'host': 'localhost', 'password': '1', 'port': 3306, 'user': 'root'}
database = MySQLDatabase('energy_wiki', **settings)
database.connect()


class Dashboard(Model):
    # 将id设定为主键和自动增加
    # id = IntegerField(primary_key=True, sequence=True)
    id = AutoField(primary_key=True)
    name = CharField()
    desc = CharField()
    html_file = CharField()

    class Meta:
        database = database


if __name__ == "__main__":
    if not Dashboard.table_exists():
        Dashboard.create_table()

