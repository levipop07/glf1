import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files['gefaengnisse.db'])
  cursor = conn.cursor()
  gefaegnisse = list(cursor.execute("SELECT GID,Name FROM Gefaengnisse"))
  print(gefaegnisse)
  return [('TODO 1', 1), ('TODO 2', 2)]




