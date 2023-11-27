from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name=self.text_box_1.text
    instagram=self.text_box_2.text
    indian=self.check_box_1.checked
    west=self.check_box_2.checked
    bugs=self.check_box_3.checked
    sun=self.check_box_4.checked
    caps=self.check_box_5.checked
    hair=self.check_box_6.checked
    sneakers=self.check_box_7.checked
    heels=self.check_box_8.checked
    wedges=self.check_box_9.checked
    flat=self.check_box_10.checked
    jewellery=self.check_box_11.checked
    
