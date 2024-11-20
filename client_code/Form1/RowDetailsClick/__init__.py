from ._anvil_designer import RowDetailsClickTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowDetailsClick(RowDetailsClickTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Details_click(self, **event_args):
    """This method is called when the button is clicked"""
    # get Form1
    parent = self.parent.parent.parent.parent
    zellennummer = self.item['zellennummer']
    data = anvil.server.call('get_data_inhaft', zellennummer)
    print(data)

    dic = []
    for x in data:
      dic.append({'haeftlingsnummer': x[0], 'einzug': x[1], 'auszug': x[2], 'haftdauer': f'{x[1]}  {x[2]}'})

    parent.repeating_panel_zellendetails.items = dic