# Shop Billing System (menu-driven): display products, add items to cart and view the total bill. Uses dict, list, set, tuples, recursion and handles ValueError, ZeroDivisionError, TypeError, NameError

# product details as tuples: (name, price, category)
PRODUCT_DETAILS = (
    ("Pen", 10, "Stationery"),
    ("Notebook", 50, "Paper"),
    ("Pencil", 5, "Stationery"),
)
 
products = {}        # {name: price}
categories = set()   # unique product categories
cart = []            # list of (name, price, quantity)
 
for name, price, category in PRODUCT_DETAILS:
    products[name] = price
    categories.add(category)
 
 
def recursive_total(items, index=0):
    """Recursively calculate the total price of all items in the cart."""
    if not isinstance(items, list):
        raise TypeError("Cart must be a list.")
    if index == len(items):
        return 0
    name, price, qty = items[index]
    if not isinstance(price, (int, float)) or not isinstance(qty, int):
        raise TypeError("Wrong data type in cart for item: " + str(name))
    return price * qty + recursive_total(items, index + 1)
 
 
def display_products():
    """Display all available products."""
    print("\nAvailable Products:")
    for name, price in products.items():
        print(name, ":", price)
 
 
def add_item():
    """Add a product and its quantity to the cart."""
    name = input("Enter product name: ").strip().title()
    if name not in products:
        raise NameError("Product '" + name + "' does not exist.")
 
    qty = int(input("Enter quantity: "))          # may raise ValueError
    if qty <= 0:
        raise ValueError("Quantity must be positive.")
 
    cart.append((name, products[name], qty))
    print(name, "x", qty, "added to cart.")
 
 
def view_total_bill():
    """Show the total bill and the average price per item."""
    if not cart:
        print("Cart is empty.")
        return
    total = recursive_total(cart)                 # may raise TypeError
    total_qty = sum(item[2] for item in cart)
    average = total / total_qty                   # may raise ZeroDivisionError
    print("\nItems in Cart:")
    for name, price, qty in cart:
        print(name, ":", price, "x", qty, "=", price * qty)
    print("Total Bill:", total)
    print("Average Price per Item:", average)
 
 
def main():
    while True:
        print("\n1. Display Products")
        print("2. Add Item to Cart")
        print("3. View Total Bill")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
 
        try:
            if choice == "1":
                display_products()
            elif choice == "2":
                add_item()
            elif choice == "3":
                view_total_bill()
            elif choice == "4":
                print("Thank you for shopping!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
        except ValueError:
            print("Error: Invalid quantity. Enter a positive whole number.")
        except ZeroDivisionError:
            print("Error: Calculation error (total quantity is zero).")
        except TypeError as e:
            print("Error: Wrong data type in cart.", e)
        except NameError as e:
            print("Error:", e)
 
 
if __name__ == "__main__":
    main()

