#from locale import currency


with open('currency_converter/currencydata.txt') as f:
  lines = f.readlines()

currencydict = {}
for line in lines:
  part = line.split("\t")
  currencydict[part[0]] = part[1]


amount = int(input("Enter amount :\n"))
print("Enter the name of currency you want to convert :\n")
print("Available options: \n")
[print(item) for item in currencydict.keys()]
currency = input("Please enter one these values :\n")

print(f"{amount} INR is equal to {amount * float(currencydict[currency])} {currency}")