#create empty list
respones = {}

current_polling_state = True

while current_polling_state:
    full_name = input(f"What is your full name? ")
    candidate = input(f"you would like to vote for? ")

    respones[full_name] = candidate

    a = input(f"Would you like to vote again? Yes or No")
    if a.lower() == 'no':
        break
print(respones)








