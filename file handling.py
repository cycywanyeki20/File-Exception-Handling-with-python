"""
Python’s built-in open() function is at the heart of this process, and learning how to handle files can make your programs more robust, flexible, and useful.
Opening Files 🔓

Use Python’s open() function to access a file.
Syntax: open(filename, mode), where:
filename: The name of the file you want to work with.
mode: The mode you want to open the file in.
Modes include:
'r': Read mode, used for reading files.
'w': Write mode, creates a new file or overwrites an existing one.
'a': Append mode, adds new content without deleting existing data.
'rb', 'wb': Binary modes for non-text files, like images.

Example:
"""
file= open("example.txt", "r") #opens file in read mode.

"""
Python provides multiple ways to read file contents:
.read(): Reads the entire file.
.readline(): Reads a single line at a time.
.readlines(): Reads all lines and returns a list.
Example:
"""

with open("example.txt", "r") as file: data = file.read() 
print(data)
#use cases: processing large datasets or analyzing taxt documents.

"""
Writing & Appending to Files ✍️

Writing is essential for saving data, like storing a user’s progress or keeping a record.
write(): Overwrites content, while append() allowing adding without deleting.
"""
with open ("output.txt", "w") as file:file.write("Hello, Python!")

"""
Closing Files: 
Files should be closed after processing to release system resources.
Python’s with statement automatically handles closing, ensuring efficient resource management.
"""

