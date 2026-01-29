# IF Problem: given the gross salary of a person, calculate the net

gross = input("What is your gross salary? ")
gross = int(gross)

if gross>4000:
    net = 0.82*gross
    print(net)
elif gross >= 2000:
    net = 0.86*gross
    print(net)
elif gross >= 1000:
    net = 0.88*gross
    print(net)
else:
    net = 0.9*gross
    print(net)

