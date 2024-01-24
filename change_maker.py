#take an input of what the user wants and how much they are paying
price = float(input("What is the cost of your item? "))
payment = float(input("Please insert payment: "))

#subtract the price from the payment and convert to pennies
change = (payment * 100) - (price * 100)

#add the dollars and cents as variables in terms of pennies
twenty = 2000
ten = 1000
five = 500
one = 100
quarter = 25
dime = 10
nickel = 5 
penny = 1

#iterate through each dollar/coin amount and replace the change variable with the modulous of itself mod cash amount
print("Price of the item:" + str(price))
print("Cash Tendered: " + str(payment))
print("Change left in pennies: ", change)

print("Twenties:", change // twenty)
change = change % twenty
print("Tens: ", change // ten)
change = change % ten
print("Fives: ", change // five)
change = change % five
print("Ones: ", change // one)
change = change % one
print("Quarters: ", change // quarter)
change = change % quarter
print("Dimes: ", change // dime)
change = change % dime
print("Nickels: ", change // nickel)
change = change % nickel
print("Pennies: ", change // penny)