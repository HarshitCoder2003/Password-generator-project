import random
import string
from colorama import init, Fore, Style

# Initialize colorama (necessary on Windows)
init()

# Define ascii_letter if needed
ascii_letter = string.ascii_letters

def generate_password(length):
    characters = ascii_letter + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

# Example usage
password_length = 10
generated_password = generate_password(password_length)
print_with_color("Generated Password:", color=Fore.CYAN, brightness=Style.BRIGHT)
print_with_color(generated_password, color=Fore.YELLOW, brightness=Style.BRIGHT)
