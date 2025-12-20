from strength_checker import PasswordStrengthChecker


def title():
    print("="*50)
    print("PASSWORD STRENGTH CHECKER")
    print("="*50)

def main():
    """
    Main function to run the password strength checker.
    """
    
    while True:
        print("\n" + "-"*50)
        print("Options:")
        print("  1. Check a password")
        print("  2. Check multiple passwords")
        print("  3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()

        validate_input(choice)


def validate_input(choice: str = "1"):
    checker = PasswordStrengthChecker("weak_passwords.txt")

    if choice == "1":
        password = input("Enter password to check: ").strip()
        checker.evaluate_password(password)
        
    elif choice == "2":
        checker.evaluate_multiple_passwords()
    elif choice == "3":
        print("\nGoodbye!")
        exit(0)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    title()
    main()