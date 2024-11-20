import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  con = sqlite3.connect(data_files["gefaengnis.db"])
  cur = con.cursor()
  data1 = list(cur.execute("SELECT name, GID FROM Gefaengnis"))
  con.commit()
  con.close()
  return data1

@anvil.server.callable
def get_boss(GID):
  con = sqlite3.connect(data_files["gefaengnis.db"])
  cur = con.cursor()
  data1 = list(cur.execute(f"SELECT Direktor FROM Verwaltung WHERE VID = {GID}"))
  con.commit()
  con.close()
  return data1[0][0]


@anvil.server.callable
def get_free_room(GID):
  con = sqlite3.connect(data_files["gefaengnis.db"])
  cur = con.cursor()
  free = list(cur.execute(f"SELECT AnzFreieZellen FROM Verwaltung WHERE VID = {GID}"))
  con.commit()
  con.close()
  return free[0][0]


@anvil.server.callable
def get_zelle_insassen():

  con = sqlite3.connect(data_files["gefaengnis.db"])
  cur = con.cursor()
  data = list(cur.execute("SELECT ZID, HID FROM Häftling")) # ich würde dort ein GROUPBY verwenden um die zellen zu grupieren aber ich weiß nicht wie :(

  print(data)
  return data

@anvil.server.callable
def get_data_inhaft(ZID):
  con = sqlite3.connect(data_files["gefaengnis.db"])
  cur = con.cursor()
  data = list(cur.execute(f"SELECT HID, Auszug, Einzug FROM Häftling WHERE ZID = {ZID}"))
  con.commit()
  con.close()
  return data
  
  