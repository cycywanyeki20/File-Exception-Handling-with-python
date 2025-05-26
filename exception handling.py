"""Exception handling is the art of catching errors and handling them gracefully. The basic structure of try-except blocks;
try: runs code that might throw an error
except: catches the error allowing you to respond without crashing
"""
try:
    with open("nonexistent.txt", "r") as file:
        data= file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")


"""
Advanced error handling with finally and custom errors.
finally: Runs no matter what, often used to clean up (like closing a file)
Custome Errors: Create custon exceptins for special cases(eg, EmptyFileError)
"""
try:
    file= ("sample.txt", "r")
    data=file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()

"""
Best Practices:
Use with for file handling: Auto-close files, preventing potential leaks.
Check file existence before reading/writing, to avoid crashes.
Handle specific exceptions over general ones (e.g., FileNotFoundError instead of Exception).
Document error messages clearly for easier debugging and user support.
"""
