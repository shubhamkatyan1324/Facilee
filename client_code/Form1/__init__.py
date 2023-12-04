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

 
    """This method is called when the button is clicked"""
    #name=self.text_box_1.checked
    #instagram=self.text_box_2.checked
    #indian=self.check_box_1.checked
    #west=self.check_box_2.checked
    #bugs=self.check_box_3.checked
    #sun=self.check_box_4.checked
    #caps=self.check_box_5.checked
    #hair=self.check_box_6.checked
    #sneakers=self.check_box_7.checked
    #heels=self.check_box_8.checked
    #wedges=self.check_box_9.checked
    #flat=self.check_box_10.checked
    #jewellery=self.check_box_11.checked
    #anvil.server.call('submit',name=name,instagram=instagram,indian=indian,west=west,bugs=bugs,sun=sun,caps=caps,hair=hair,sneakers=sneakers,heels=heels,wedges=wedges,flat=flat,jewellery=jewellery)
    #Notification("your response is recorded")

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    alert('you selected the category ' + self.drop_down_1.selected_value)

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    alert('You selected the category ' + self.drop_down_2.selected_value )

  def drop_down_3_change(self, **event_args):
    """This method is called when an item is selected"""
    alert('you selected the category ' + self.drop_down_3.selected_value)

  def drop_down_4_change(self, **event_args):
    """This method is called when an item is selected"""
    alert('you selected the category ' + self.drop_down_4.selected_value)

  def drop_down_5_change(self, **event_args):
    """This method is called when an item is selected"""
    alert('you selected the category ' + self.drop_down_5.selected_value)

  def drop_down_6_change(self, **event_args):
    """This method is called when an item is selected"""
    alert('you selected the category ' + self.drop_down_6.selected_value)

  def drop_down_7_change(self, **event_args):
    """This method is called when an item is selected"""
    alert('you selected the category ' + self.drop_down_7.selected_value)

  def drop_down_8_change(self, **event_args):
    """This method is called when an item is selected"""
    alert('you selected the category ' + self.drop_down_8.selected_value)

  #def drop_down_9_change(self, **event_args):
    """This method is called when an item is selected"""
    #alert('you selected the category ' + self.drop_down_9.selected_value)

  #def drop_down_10_change(self, **event_args):
    """This method is called when an item is selected"""
    #alert('you selected the category ' + self.drop_down_10.selected_value)

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    alert('you selected the category sports')

  def check_box_2_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    alert('you selected the category Anime ')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    instagramHandle = self.text_box_2.text
    home = self.drop_down_1.selected_value
    phone = self.drop_down_2.selected_value
    jewellery = self.drop_down_3.selected_value
    beauty = self.drop_down_4.selected_value
    accessories = self.drop_down_5.selected_value
    footwear = self.drop_down_6.selected_value
    clothing = self.drop_down_7.selected_value
    arts = self.drop_down_8.selected_value
    sports = self.check_box_1.checked
    anime = self.check_box_2.checked
    anvil.server.call('submit' , name=name,instagramHandle=instagramHandle,home=home,phone=phone,jewellery=jewellery,beauty=beauty,accessories=accessories,footwear=footwear,clothing=clothing,arts=arts,sports=sports,anime=anime)
    Notification("your Response has been recorded ").show()
    

 
    

  
