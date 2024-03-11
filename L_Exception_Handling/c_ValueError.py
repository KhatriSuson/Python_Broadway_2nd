promt = "how many tickets do you need"
num_tickets = input(promt)

try:
    num_tickets = int(num_tickets)
except ValueError as e:
    print("Please try again.", e)

else:
    print("Your tickets are printing.")