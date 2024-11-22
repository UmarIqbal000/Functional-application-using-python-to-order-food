# Define the menu
menu = {
    "Pizza": 8.99,
    "Burger": 5.49,
    "Pasta": 7.99,
    "Salad": 4.99,
    "Soda": 1.99
}

# Initialize an empty cart
cart = {}

# Function to display the menu
def view_menu():
    print("\n--- Menu ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print()

# Function to add an item to the cart
def add_to_cart():
    view_menu()
    item = input("Enter the item you want to add to your cart: ").title()
    if item in menu:
        quantity = int(input(f"How many {item}s would you like to add? "))
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"{quantity} {item}(s) added to your cart.")
    else:
        print("Sorry, that item is not on the menu.")

# Function to remove an item from the cart
def remove_from_cart():
    if not cart:
        print("Your cart is empty. Nothing to remove.")
        return
    view_cart()
    item = input("Enter the item you want to remove from your cart: ").title()
    if item in cart:
        quantity = int(input(f"How many {item}s would you like to remove? "))
        if quantity >= cart[item]:
            del cart[item]
            print(f"{item} removed from your cart.")
        else:
            cart[item] -= quantity
            print(f"{quantity} {item}(s) removed from your cart.")
    else:
        print(f"{item} is not in your cart.")

# Function to view the cart
def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\n--- Your Cart ---")
        total = 0
        for item, quantity in cart.items():
            price = menu[item] * quantity
            total += price
            print(f"{item} (x{quantity}): ${price:.2f}")
        print(f"Total: ${total:.2f}")
        print()

# Function to place the order
def place_order():
    if not cart:
        print("Your cart is empty. Add items to your cart before placing an order.")
    else:
        view_cart()
        confirm = input("Would you like to place the order? (yes/no): ").lower()
        if confirm == "yes":
            print("Thank you for your order! Your food will be ready soon.")
            cart.clear()
        else:
            print("Order canceled.")

# Main loop
def main():
    while True:
        print("\n--- Food Ordering System ---")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Place Order")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            view_menu()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            place_order()
        elif choice == "6":
            print("Thank you for using the Food Ordering System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
