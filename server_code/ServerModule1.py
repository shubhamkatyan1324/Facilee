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
def submit(name,instagram,indian,west,bugs,sun,caps,hair,sneakers,heels,wedges,flat,jewellery):
  app_tables.facile.add_row(name=name,instagram=instagram,indian=indian,west=west,bugs=bugs,sun=sun,caps=caps,hair=hair,sneakers=sneakers,heels=heels,wedges=wedges,flat=flat,jewellery=jewellery)
  
