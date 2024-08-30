shopping_list = []

def show_menu():
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def view_list():
    if shopping_list:
        print("\nShopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The list is empty.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_list()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
    
    
    