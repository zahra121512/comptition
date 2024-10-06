def get_ascii_value(character):
    """Gets the ASCII value of a given character.

    Args:
        character: The character to get the ASCII value of.

    Returns:
        The ASCII value of the character.
    """

    try:
        return ord(character)
    except TypeError:
        print("Error: Please enter a valid character.")
        return None

def main():
    """Main function to get user input and display the ASCII value."""

    while True:
        character = input("Enter a character: ")
        ascii_value = get_ascii_value(character)

        if ascii_value is not None:
            print(f"The ASCII value of '{character}' is {ascii_value}.")
        else:
            break

if __name__ == "__main__":
    main()