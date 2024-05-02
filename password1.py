# Function to display menu options
def display_menu():
    print("1. Store Password")
    print("2. Retrieve Password")
    print("3. Exit")
# Function to store password
def store_password():
    account_name = input("Enter Account Name: ")
    password = input("Enter Password: ")
    passwords[account_name] = password
    print("Password stored successfully!")
# Function to retrieve password
def retrieve_password():
    account_name = input("Enter Account Name: ")
    if account_name in passwords:
        print("Password:", passwords[account_name])
    else:
        print("Account not found!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            store_password()
        elif choice == '2':
            retrieve_password()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Dictionary to store passwords
passwords = {}

# Entry point of the program
if __name__ == "__main__":
    main()