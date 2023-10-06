#!/usr/bin/python3

"""
    initialize the models package
"""

from models.engine.storage import Storage
import os


DB_NAME = os.getenv("DATABASE")
DB_USERNAME = os.getenv("USERNAME")
DB_PASSWORD = os.getenv("PASSWORD")
DB_HOST = os.getenv("HOST")


DB_URL = f"mysql+mysqldb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

storage = Storage(DB_URL)
storage.reload()
