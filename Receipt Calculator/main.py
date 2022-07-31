"""
we use pretty table library to create out Receipt Calculator
to install pretty table : pip install prettytable
Generating PrettyTable :

Initialisation :
<table name> = PrettyTable(['<column1>','<column2>',....])

To add a row :
<table name> .add_row(['<row1>','<row2>',....])

"""


from prettytable import PrettyTable
  
  
print('--------------WELCOME TO Vmart Shop--------------\n')
table = PrettyTable(['Item Name', 'Item Price'])
total = 0

print("Enter item name and price or press q key on keyboard to quit")
while(True):
  name = input("Enter Item name : ")
  if (name != 'q'):
    price = int(input("Enter The Price : "))
    total=total+price
    table.add_row([name,price])
    continue
  else:
    break

table.add_row (['Total',total])
print(table)
print('\nThanks for shopping with us :)')
print(f'Your total bill amount is {total} /-')

