with open('data.txt') as f:
    lines=f.readlines()

currencydict={}
for line in lines:
    a=line.split("\t")
    currencydict[a[0]]=a[1]

amount = int(input("Enter amount:\n"))
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencydict.keys()]   
currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount *float(currencydict[currency])} {currency}")