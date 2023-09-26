#!/usr/bin/python3

"""
    initialize the models package
"""

from models.engine.storage import Storage
import os

ENV = os.getenv("ENV")

if ENV == "DEVELOPMENT" or ENV == "TEST":
    DB_NAME = "alpha_alchemy_dev_db"
    DB_USERNAME = "alpha_dev"
    DB_PASSWORD = "alpha_Dev1"
else:
    DB_NAME = os.getenv("DATABASE")
    DB_USERNAME = os.getenv("USERNAME")
    DB_PASSWORD = os.getenv("PASSWORD")


DB_URL = f"mysql+mysqldb://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}"

storage = Storage(DB_URL)
storage.reload()
