import re

def check_password_strength(password):
    # Define regex patterns to match different criteria
    patterns = {
        'length': r'.{8,}',             # At least 8 characters 
        'uppercase': r'[A-Z]',          # At least one uppercase letter
        'lowercase': r'[a-z]',          # At least one lowercase letter
        'number': r'[0-9]',             # At least one digit
        'special': r'[$&+,:;=?@#|\'<>.^*()%!-]'  # At least one special character
    }

    # Check if the password meets each criteria
    def meets_criteria(pattern):
        return re.search(patterns[pattern], password) is not None

    # Evaluate the strength of the password
    is_length_valid = meets_criteria('length')
    has_uppercase = meets_criteria('uppercase')
    has_lowercase = meets_criteria('lowercase')
    has_number = meets_criteria('number')
    has_special_char = meets_criteria('special')

    # Determine password strength based on criteria met
    strength = 'Weak'
    if is_length_valid and has_uppercase and has_lowercase and has_number and has_special_char:
        strength = 'Strong'
    elif is_length_valid and (has_uppercase or has_lowercase or has_number or has_special_char):
        strength = 'Moderate'

    return strength

def main():
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
