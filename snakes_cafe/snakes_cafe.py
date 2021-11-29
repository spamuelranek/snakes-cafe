appetizers_list = ["Wings","Cookies","Spring Rolls"]
entrees_list = ["Salmon","Steak","Meat Tornado","A Literal Garden"]
desserts_list = ["Ice Cream", "Cake", "Pie"]
drinks_list = ["Coffee", "Tea", "Unicorn Tears"]

def list_items(list):
  str_list = ""
  for item in list:
    if len(str_list) == 0:
      str_list = item
    else:
      str_list = str_list + "\n" +item
  return str_list

appetizers = list_items(appetizers_list)
entrees = list_items(entrees_list)
desserts = list_items(desserts_list)
drinks = list_items(drinks_list)

header = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""
appetizers_headers = """
Appetizers
----------"""
entrees_headers = """
Entrees
-------"""
desserts_headers = """
Desserts
--------"""
drinks_headers = """
Drinks
------"""
order_question = """***********************************
** What would you like to order? **
***********************************"""

menu = [header,appetizers_headers,appetizers,entrees_headers,entrees,desserts_headers,desserts,drinks_headers,drinks,""]

def create_menu(list):
  for item in list:
    print(item)

create_menu(menu)

def order_from_menu():
  print(order_question)
  x = True
  order_dict={}
  while x:
    order = input("> ")
    if order == "quit":
      x = False
    else:
      if order in order_dict.keys():
        order_dict[order] += 1
      else:
        order_dict[order] = 1
      num = order_dict[order]
      if num == 1:
        order_s = "order"
      else:
        order_s = "orders"
      order_format = f"{num} {order_s} of {order} have been added to your meal"
      print(order_format)

order_from_menu()