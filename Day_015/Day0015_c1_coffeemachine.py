Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

# TODO: 

# 1. Print report of all resources.

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    """Prints a report of all resources."""
    print("📋 Resource Report:")
    for resource, amount in resources.items():
        if resource == "money":
            print(f"💰 {resource.capitalize()}: ${amount}")
        else:
            print(f"💧 {resource.capitalize()}: {amount}ml")

# 2. Check if resources are sufficient to make a drink.

def is_resource_sufficient(order_ingredients):
    """Returns True if resources are sufficient to make the drink, False otherwise."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"❌ Sorry, there is not enough {item}.")
            return False
    return True

# 3. Process coins.

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("💵 Please insert coins.")
    total = int(input("How many quarters? (0.25): ") or "0") * 0.25
    total += int(input("How many dimes? (0.10): ") or "0") * 0.10
    total += int(input("How many nickels? (0.05): ") or "0") * 0.05
    total += int(input("How many pennies? (0.01): ") or "0") * 0.01
    return total

# 4. Check transaction successful?

def is_transaction_successful(money_received, drink_cost):
    """Return True if the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"✅ Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("❌ Sorry, that's not enough money. Money refunded.")
        return False

# 5. Make Coffee.

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"☕ Here is your {drink_name}. Enjoy!")

def coffee_machine():
    """Main function to run the coffee machine."""
    print("☕ Welcome to the Coffee Machine! ☕")
    print("\n📋 Menu:")
    for drink_name, drink_info in Menu.items():
        print(f"  {drink_name.capitalize()}: ${drink_info['cost']}")
    print()
    is_on = True
    drink_options = {"1": "espresso", "2": "latte", "3": "cappuccino"}

    while is_on:
        choice = input("What would you like? (1)Espresso (2)Latte (3)Cappuccino: ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print_report()
        elif choice in drink_options:
            drink_name = drink_options[choice]
            drink = Menu.get(drink_name)
            if drink and is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(drink_name, drink["ingredients"])
                    print("🙏 Thank you for your order!")

if __name__ == "__main__":
    coffee_machine()