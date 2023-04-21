"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13kd8rddl13a583efg-a.oregon-postgres.render.com",
        database="todo_h800",
        user="todo_h800_user",
        password="RZNhSuVZIzkWtvaYyShMpRnCwgcUFMXM")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
