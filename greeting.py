# Personalized Greeting Program

# Define a function named 'personalized_greeting'
def personalized_greeting():
    # Prompt the user to input their name and store it in the variable 'name'
    name = input("What is your name? ")
    # Prompt the user to input their favorite color and store it in the variable 'color'
    color = input("What is your favorite color? ")
    # Print a personalized greeting message using the user's name and favorite color
    print(f"Hello, {name}! Your favorite color, {color}, is awesome!")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the 'personalized_greeting' function to execute the greeting logic
    personalized_greeting()