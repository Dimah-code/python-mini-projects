import re
import hashlib
import string
from typing import List

from models.password import Password

class PasswordStrengthChecker:
    def __init__(self, weak_passwords_file="weak_passwords.txt"):
        """
        Initialize the password strength checker.
        Loads weak passwords from a file for comparison.
        """
        self.weak_passwords = self.load_weak_passwords(weak_passwords_file)
    
    def load_weak_passwords(self, filename) -> list:
        """
        Load weak passwords from a file.
        Returns a list of weak passwords.
        """
        weak_passwords = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    password = line.strip()
                    if password:
                        weak_passwords.append(password)
                
            print(f"Loaded {len(weak_passwords)} weak passwords from '{filename}'")
        except FileNotFoundError:
            print(f"Warning: File '{filename}' not found. Continuing without weak password list.")
        except Exception as e:
            print(f"Error loading weak passwords: {e}")
        
        return weak_passwords
    
    def check_against_weak_list(self, password) -> bool:
        """
        Check if the password exists in the weak password list.
        Returns True if password is weak, False otherwise.
        """
        # Check the password and its lowercase version
        return password in self.weak_passwords or password.lower() in self.weak_passwords
    
    def check_password_strength(self, password) -> Password:
        """
        Check the strength of a password.
        Returns a Password.
        """
        if not password:
            return 0, "Password cannot be empty"
        
        result = Password()
        result.password = password
        # Initial checks
        is_too_short = len(password) < 8
        is_weak_password = self.check_against_weak_list(password)
        
        # Calculate strength score
        score = 0
        feedback = []
        
        # Length check
        if is_too_short:
            feedback.append("Password should be at least 8 characters long")
        else:
            score += 1
        
        if len(password) >= 12:
            score += 1
        if len(password) >= 16:
            score += 1
        
        # Character variety checks
        has_lowercase = any(c.islower() for c in password)
        has_uppercase = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        if has_lowercase:
            score += 1
        else:
            feedback.append("Password should contain at least one lowercase letter")
        
        if has_uppercase:
            score += 1
        else:
            feedback.append("Password should contain at least one uppercase letter")
        
        if has_digit:
            score += 1
        else:
            feedback.append("Password should contain at least one digit")
        
        if has_special:
            score += 1
        else:
            feedback.append("Password should contain at least one special character")
        
        # Check for common patterns
        common_patterns = [
            "123", "abc", "qwerty", "password", "admin", "letmein",
            "welcome", "monkey", "dragon", "sunshine"
        ]
        
        password_lower = password.lower()
        for pattern in common_patterns:
            if pattern in password_lower:
                score -= 1
                feedback.append(f"Avoid common patterns like '{pattern}'")
                break
        
        # Check for sequential characters
        sequential_count = 0
        for i in range(len(password) - 2):
            if (ord(password[i]) + 1 == ord(password[i+1]) and 
                ord(password[i+1]) + 1 == ord(password[i+2])):
                sequential_count += 1
        
        if sequential_count > 0:
            score -= min(sequential_count, 2)
            feedback.append("Avoid sequential characters (e.g., abc, 123)")
        
        # Check if password is in weak list
        if is_weak_password:
            score = 0
            feedback.append("This password is in the weak password list - choose a different one")
        
        # Determine strength level
        if score <= 3 or is_too_short or is_weak_password:
            strength = "Very Weak"
        elif score <= 5:
            strength = "Weak"
        elif score <= 7:
            strength = "Moderate"
        elif score <= 9:
            strength = "Strong"
        else:
            strength = "Very Strong"
        
        result.feedback = feedback
        result.score = score
        result.strength = strength

        return result
    
    def evaluate_password(self, password) -> Password:
        """
        Evaluate password and print detailed results.
        """
        print("\n" + "="*50)
        print("PASSWORD STRENGTH ANALYSIS")
        print("="*50)
        
        password_result = self.check_password_strength(password)
        
        print(f"Password: {'*' * len(password)}")
        print(f"Length: {len(password)} characters")
        print(f"Strength Score: {password_result.score}/10")
        print(f"Strength Level: {password_result.strength}")
        
        if password_result.feedback:
            print("\nRecommendations:")
            for message in password_result.feedback:
                print(f"  - {message}")
        else:
            print("\n✓ Good job! Your password meets all basic security requirements.")
        
        # Additional security tips
        if password_result.strength in ["Very Weak", "Weak"]:
            print("\n   SECURITY WARNING: This password is not secure!")
            print("   Consider using a passphrase or password manager.")
        
        return password_result
    
    def check_multiple_passwords(self, passwords: list) -> List[Password]:
        """
        Check multiple passwords at once.
        """
        results: List[Password] = []
        for password in passwords:
            password_result = self.check_password_strength(password)
            results.append(password_result)
        
        return results

    def get_multiple_passwords(self) -> list:
        passwords = []
        print("\nEnter passwords to check (enter 'done' when finished):")
        while True:
            password = input("Password: ").strip()
            if password.lower() == 'done':
                break
            passwords.append(password)
        return passwords
            
    def evaluate_multiple_passwords(self) -> None:
        passwords = self.get_multiple_passwords()
        if passwords:
            results = self.check_multiple_passwords(passwords)
            print("\n" + "-"*50)
            print("MULTIPLE PASSWORD ANALYSIS")
            print("-"*50)
            for result in results:
                masked = '*' * len(result.password) if len(result.password) > 3 else '***'
                print(f"Password: {masked:<15} | Score: {result.score}/10 | Strength: {result.strength}")

