# Inventory Manager CLI

A simple command-line inventory management application written in Python.

This is my first Python project. The program allows users to manage a small inventory, add and update products, remove products, save data to a JSON file, and generate a basic stock summary.

## Features

- Show current inventory
- Add new products
- Update existing product quantity
- Update product price
- Remove products from inventory
- Save inventory data to a JSON file
- Load inventory data from a JSON file
- Calculate total product quantity
- Calculate average product quantity
- Find product with the highest quantity
- Find product with the lowest quantity
- Check shortages based on a minimum stock level
- Calculate restocking cost
- Compare restocking cost with available budget
- Basic input validation
- Clear console during program flow

## Technologies used

- Python
- JSON
- Command-line interface

## How to run

1. Clone the repository or download the files.
2. Make sure Python is installed on your computer.
3. Open the project folder in a terminal.
4. Run the program:

```bash
python inventory_manager.py
```

or:

```bash
py inventory_manager.py
```

## Example usage

The program asks the user for:

- shopping budget
- minimum stock quantity
- product name
- product quantity
- product price

Example product data is saved in `inventory.json`:

```json
{
    "Apples": {
        "quantity": 10,
        "price": 3
    },
    "Bananas": {
        "quantity": 5,
        "price": 4
    }
}
```

## What I learned

While building this project, I practiced:

- Python functions
- loops
- dictionaries
- nested dictionaries
- working with user input
- input validation
- error handling with `try` and `except`
- reading and writing JSON files
- basic CRUD operations
- simple business logic
- organizing code into functions
- using a `main()` function

## Future improvements

Possible future improvements:

- Add a menu system
- Add search product feature
- Add product categories
- Add total inventory value calculation
- Save reports to a text file
- Split the code into multiple files
- Add unit tests
- Replace JSON storage with a database

## Project status

Version 1.0 completed as a learning project.