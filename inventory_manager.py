# Inventory Manager CLI
# A simple command-line inventory management application.
# Features: add, update, remove products, save/load JSON data,
# calculate stock summary, check shortages and restocking budget.


# # IMPORTS # #

import os
import json


# # FUNCTIONS # #

def main():
    inventory = load_inventory("inventory.json")

    print("Current inventory:")
    show_inventory(inventory)

    budget = get_number("Enter your shopping budget: ")
    clear_console()

    if budget == 0:
        print("No budget available.")
        exit()

    minimum = get_number("Enter the minimum quantity: ")
    clear_console()

    stop_words = [
        "end",
        "none",
        "null",
        "nothing",
        "zero",
        "stop",
        "pause",
        "break"
    ]

    while True:
        product_name = input("Enter product name: ").strip()
        product_name_check = product_name.lower()
        clear_console()

        if product_name == "":
            print("Product name cannot be empty.")
            continue

        if product_name_check in stop_words:
            clear_console()
            break

        product_name = product_name.capitalize()

        product_quantity = get_number("Enter product quantity in stock: ")
        clear_console()

        product_price = get_number("Enter product price: ")
        clear_console()

        if product_name in inventory:
            inventory[product_name]["quantity"] += product_quantity
            inventory[product_name]["price"] = product_price
        else:
            inventory[product_name] = {
                "quantity": product_quantity,
                "price": product_price
            }


    should_remove = input("Do you want to remove a product? yes/no: ").strip().lower()
    clear_console()
    show_inventory(inventory)


    if should_remove == "yes":
        remove_product(inventory)
        clear_console()

    if len(inventory) == 0:
        save_inventory(inventory, "inventory.json")
        print("The inventory is empty. Program finished.")
        exit()


    show_summary(inventory)

    total_shortages, shortage_cost, shortage_details = check_shortages(inventory, minimum)


    if len(shortage_details) == 0:
        print("Nothing needs to be restocked.")
    else:
        print("Shortages to restock:")

        for shortage in shortage_details:
            print("-", shortage)

        print("Total missing:", total_shortages, "pieces")
        print("Restock cost:", shortage_cost, "PLN")

        check_budget(shortage_cost, budget)


    print("Inventory after update:")
    show_inventory(inventory)

    save_inventory(inventory, "inventory.json")

def get_number(message):
    while True:
        try:
            number = int(input(message))
            if number < 0:
                print("The number cannot be negative. Please try again")
                continue
            return number
        except ValueError:
            print("You entered an invalid number. Please try again.")


def save_inventory(inventory, file_name):
    with open(file_name, "w") as file:
        json.dump(inventory, file, indent=4)


def load_inventory(file_name):
    try:
        with open(file_name, "r") as file:
            inventory = json.load(file)
            return inventory
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def show_product(name, quantity, price):
    print(f"{name} - quantity: {quantity}, price per piece: {price} PLN")


def show_inventory(inventory):
    if len(inventory) == 0:
        print("The inventory is empty.")
    else:
        for name in inventory:
            quantity = inventory[name]["quantity"]
            price = inventory[name]["price"]

            show_product(name, quantity, price)


def calculate_total_quantity(inventory):
    total_quantity = 0

    for name in inventory:
        quantity = inventory[name]["quantity"]
        total_quantity += quantity

    return total_quantity


def calculate_average_quantity(inventory):
    total = calculate_total_quantity(inventory)
    average = total / len(inventory)

    return average


def find_product_with_highest_quantity(inventory):
    highest_quantity = 0
    highest_product_name = ""

    for name in inventory:
        quantity = inventory[name]["quantity"]

        if quantity > highest_quantity:
            highest_quantity = quantity
            highest_product_name = name

    return highest_quantity, highest_product_name


def find_product_with_lowest_quantity(inventory):
    first_product = list(inventory.keys())[0]
    lowest_quantity = inventory[first_product]["quantity"]
    lowest_product_name = first_product

    for name in inventory:
        quantity = inventory[name]["quantity"]

        if quantity < lowest_quantity:
            lowest_quantity = quantity
            lowest_product_name = name

    return lowest_quantity, lowest_product_name


def check_shortages(inventory, minimum):
    total_missing_quantity = 0
    total_restock_cost = 0
    shortage_details = []

    for name in inventory:
        product_quantity = inventory[name]["quantity"]
        price = inventory[name]["price"]

        if product_quantity < minimum:
            missing_quantity = minimum - product_quantity
            restock_cost = missing_quantity * price

            total_missing_quantity += missing_quantity
            total_restock_cost += restock_cost

            shortage_details.append(
                f"{name} - missing: {missing_quantity} pieces, restock cost: {restock_cost} PLN"
            )

    return total_missing_quantity, total_restock_cost, shortage_details


def check_budget(shortage_cost, budget):
    if budget < shortage_cost:
        print("You are missing", shortage_cost - budget, "PLN to restock all shortages.")
    elif budget == shortage_cost:
        print("The budget is just enough.")
    else:
        print("You will have", budget - shortage_cost, "PLN left after restocking.")


def show_summary(inventory):
    total = calculate_total_quantity(inventory)
    print("Total products:", total, "pieces")

    average = calculate_average_quantity(inventory)
    print("Average product quantity:", round(average, 2), "pieces")

    highest_quantity, highest_product_name = find_product_with_highest_quantity(inventory)
    print("Product with the highest quantity:", highest_product_name, "-", highest_quantity, "pieces")

    lowest_quantity, lowest_product_name = find_product_with_lowest_quantity(inventory)
    print("Product with the lowest quantity:", lowest_product_name, "-", lowest_quantity, "pieces")


def remove_product(inventory):
    name = input("Enter the name of the product to remove: ").strip().capitalize()

    if name in inventory:
        del inventory[name]
        print("Removed product:", name)
    else:
        print("There is no such product in the inventory.")

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


# # MAIN PROGRAM # #

if __name__ == "__main__":
    main()