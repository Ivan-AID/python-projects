print("Welcome To Order Pizza")
def calculate_pizza_bill(size, add_pepperoni, extra_cheese):
    # Base prices
    pizza_prices = {"s": 100, "m": 125, "l": 150, "f": 200}
    pepperoni_prices = {"s": 20, "m": 40, "l": 40, "f": 50}
    cheese_price = 20

    # Calculate total
    total = pizza_prices[size]
    if add_pepperoni == "y":
        total += pepperoni_prices[size]
    if extra_cheese == "y":
        total += cheese_price

    return total

# Example usage:
size = input("Enter the size of the pizza (s/m/l/f): ").lower()
add_pepperoni = input("Do you want to add pepperoni? (y/n): ").lower()
extra_cheese = input("Do you want extra cheese? (y/n): ").lower()

total_bill = calculate_pizza_bill(size, add_pepperoni, extra_cheese)
print(f"Your total bill is: {total_bill}")

