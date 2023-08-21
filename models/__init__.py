#!/usr/bin/python3

"""
    initialize the models package
"""

from models.engine.storage import Storage

DB_URL = "mysql+mysqldb://alpha_dev:alpha_Dev1@localhost/alpha_alchemy_dev_db"

storage = Storage(DB_URL)
storage.reload()
