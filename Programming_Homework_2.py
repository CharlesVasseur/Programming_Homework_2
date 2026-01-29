# IF Problem: given the gross salary of a person, calculate the net

gross = input("What is your gross salary? ")
gross = int(gross)
child = input("To determine if you have an extra tax cut, how many children do you have? ")
child = int(child)

if gross>4000:
    net = (0.82-0.005*child)*gross
    print(net)
elif gross >= 2000:
    net = (0.86-0.01*child)*gross
    print(net)
elif gross >= 1000:
    net = (0.88-0.01*child)*gross
    print(net)
else:
    net = (0.9-0.01*child)*gross
    print(net)
