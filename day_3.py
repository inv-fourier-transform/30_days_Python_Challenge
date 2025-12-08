# Inventory system using a dictionary
def add_item(item: str,qty: int,dictionary: dict):
    if item in dictionary:
        if qty < 0:
            print("Invalid quantity")
        else:
            dictionary[item] += qty
    else:
        dictionary[item] = qty

def remove_item(item: str,qty: int,dictionary: dict):
    if item in dictionary:
        if dictionary[item] < qty:
            print("Not enough quantity in inventory")
        else:
            dictionary[item] -= qty
        if dictionary[item] == 0:
            del dictionary[item]
    else:
        print("Item not found in inventory")

def show_quantity(item,dictionary):
    if item in dictionary:
        print(f"The quantity of {item} is {dictionary[item]}")
    else:
        print("Item not found in inventory")

def display_dictionary(dictionary: dict):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    dictionary = {}
    add_item("iPhones", 9, dictionary)
    add_item("MacBooks", 5, dictionary)
    add_item("AirPods", 12, dictionary)
    add_item("iPads", 7, dictionary)
    print("Initial inventory")
    print("----------------")
    display_dictionary(dictionary)
    print("\n")
    remove_item("iPhones", 2, dictionary)
    print("After removing specified iPhones:")
    show_quantity("iPhones", dictionary)
    remove_item("MacBooks", 1, dictionary)
    print("After removing specified MacBooks:")
    show_quantity("MacBooks", dictionary)
    remove_item("AirPods", 2, dictionary)
    print("After removing specified AirPods:")
    show_quantity("AirPods", dictionary)
    remove_item("iPads", 3, dictionary)
    print("After removing specified iPads:")
    show_quantity("iPads", dictionary)
    print("----------------")
    print("Updated inventory:")
    display_dictionary(dictionary)

