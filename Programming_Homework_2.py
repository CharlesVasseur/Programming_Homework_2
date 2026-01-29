# IF Problem: given the gross salary of a person, calculate the net

gross = input("What is your gross salary? ")
try:
    gross = int(gross)
except ValueError:
    gross = input("Please enter a valid number: ")
    gross = int(gross)

child = input("To determine if you have an extra tax cut, how many children do you have? ")
try:
    child = int(child)
except ValueError:
    child = input("Please enter a valid number: ")
    child = int(child)
except int(child)<0:
    child = input("This is not a valid number of children, try again: ")
    child = int(child)

if gross>4000:
    net = (0.82+0.005*child)*gross
    tax = gross - net
    print("Your net income is ", net, ", and you should be paying ", tax, "in taxes.")
elif gross >= 2000:
    net = (0.86+0.01*child)*gross
    tax = gross - net
    print("Your net income is ", net, ", and you should be paying ", tax, "in taxes.")
elif gross >= 1000:
    net = (0.88+0.01*child)*gross
    tax = gross - net
    print("Your net income is ", net, ", and you should be paying ", tax, "in taxes.")
else:
    net = (0.9+0.01*child)*gross
    tax = gross - net
    print("Your net income is ", net, ", and you should be paying ", tax, "in taxes.")
