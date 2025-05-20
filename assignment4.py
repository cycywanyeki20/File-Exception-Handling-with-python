"""
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""

def read_and_modify_file():
    # Step 1: Ask user for input file name
    input_filename = input("Enter the name of the file to read from: ")

    try:
        # Step 2: Try to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Step 3: Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Step 4: Write modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f" Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f" Error: Could not read the file '{input_filename}'.")

# Run the function
read_and_modify_file()
