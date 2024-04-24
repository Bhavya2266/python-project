import string
import random

def generate_password(length):
    """Generate a random password of the given length."""
    # Define the set of possible characters
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by selecting characters from the set
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password

# Example usage:
print(generate_password(12))