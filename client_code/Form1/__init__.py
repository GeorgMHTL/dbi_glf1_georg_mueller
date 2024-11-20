from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')

    gid = self.gefaengnisse_drop_down.selected_value
    data = anvil.server.call('get_boss', gid)
    self.label_direktor.text = data
    
    gid = self.gefaengnisse_drop_down.selected_value
    data = anvil.server.call('get_free_room', gid)
    self.label_freie_zellen.text = data

    data = anvil.server.call('get_zelle_insassen')
    dic = []
    for x in data:
      dic.append({'zellennummer': x[0], 'anzahl_häftlinge': x[1]})
      
    self.repeating_zellen.items = dic

  def gefaengnisse_drop_down_change(self, **event_args):
    gid = self.gefaengnisse_drop_down.selected_value
    data = anvil.server.call('get_boss', gid)
    self.label_direktor.text = data
    
    gid = self.gefaengnisse_drop_down.selected_value
    data = anvil.server.call('get_free_room', gid)
    self.label_freie_zellen.text = data

 



  
 
