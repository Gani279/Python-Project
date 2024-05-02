# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:28:30 2024

@author: User
"""

from cryptography.fernet import Fernet
import json
import getpass

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.key = self.generate_key()

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_password(self, password):
        cipher_suite = Fernet(self.key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        cipher_suite = Fernet(self.key)
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password

    def save_password(self, category, website, username, password):
        encrypted_password = self.encrypt_password(password)
        entry = {
            'website': website,
            'username': username,
            'password': encrypted_password
        }

        # Load existing passwords
        try:
            with open('passwords.json', 'r') as file:
                passwords = json.load(file)
        except FileNotFoundError:
            passwords = {}

        # Save the new entry
        if category not in passwords:
            passwords[category] = {}
        passwords[category][website] = entry

        # Save the updated passwords
        with open('passwords.json', 'w') as file:
            json.dump(passwords, file, indent=2)

        print(f"Password for {website} saved successfully!")

    def retrieve_password(self, category, website):
        try:
            with open('passwords.json', 'r') as file:
                passwords = json.load(file)
        except FileNotFoundError:
            print("No passwords found. Add some passwords first.")
            return

        if category in passwords and website in passwords[category]:
            entry = passwords[category][website]
            decrypted_password = self.decrypt_password(entry['password'])
            print(f"\nWebsite: {entry['website']}\nUsername: {entry['username']}\nPassword: {decrypted_password}")
        else:
            print("Password not found.")

if __name__ == "__main__":
    master_password = getpass.getpass("Enter your master password: ")
    password_manager = PasswordManager(master_password)

    while True:
        print("\nPassword Manager Menu:")
        print("1. Save Password")
        print("2. Retrieve Password")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            category = input("Enter the category: ")
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")
            password_manager.save_password(category, website, username, password)
        elif choice == '2':
            category = input("Enter the category: ")
            website = input("Enter the website: ")
            password_manager.retrieve_password(category, website)
        elif choice == '3':
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
