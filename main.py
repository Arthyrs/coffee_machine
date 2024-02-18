from data_file import MENU, resources

MONEY = 0
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${MONEY}")

def check_resources(user_choice):
    shortcut = MENU[user_choice]['ingredients']
    shortcut["milk"] = 0
    if user_choice in MENU:
        insufficient_ingredient = ""
        for resource in resources:
            required_amount = MENU[user_choice]['ingredients'][resource]
            if resources[resource] < required_amount:
                insufficient_ingredient += resource

        if insufficient_ingredient:
            return f"Sorry there is not enough {insufficient_ingredient}."
        else:
            for resource in resources:
                resources[resource] -= MENU[user_choice]['ingredients'][resource]

def process_coins():
    global MONEY
    coin_data = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    print("Please insert coins.")
    total_value = 0
    for coin in coin_data:
        question = int(input(f"How many {coin}?: "))
        result = coin_data[coin] * question
        total_value += result
    MONEY = round(total_value, 2)

def check_transaction(user_choice):
    global MONEY
    cost_of_drink = MENU[user_choice]['cost']
    if MONEY >= cost_of_drink:
        MONEY -= cost_of_drink
    else:
        return "Sorry that's not enough money. Money refunded."

def coffee_brewer():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        return
    elif user_choice == "report":
        report()
    else:
        if check_resources(user_choice):
            print(check_resources(user_choice))
            coffee_brewer()
        else:
            process_coins()
            if check_transaction(user_choice):
                print(check_transaction(user_choice))
            else:
                print(f"Here is ${MONEY} in change.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")

    coffee_brewer()

coffee_brewer()
