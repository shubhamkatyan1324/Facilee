import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def submit(BrandName,Socialhandle,Email,Phonenumber,home,Mobile,jewellery,beauty,accessories,footwear,clothing,arts,sports,anime):
  app_tables.facile.add_row(BrandName=BrandName,Socialhandle=Socialhandle,Email=Email,Phonenumber=Phonenumber,home=home,Mobile=Mobile,jewellery=jewellery,beauty=beauty,accessories=accessories,footwear=footwear,clothing=clothing,arts=arts,sports=sports,anime=anime)

  
