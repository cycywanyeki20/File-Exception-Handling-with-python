#open a file in read mode.
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('new.txt','w')as file:
#     file.write('Hello world wwwwwww, welcome to rasa technologies webinar session'
with open('input.txt','w') as file:
    text= file.write('Welcome to my weekly coding challenge with python. THis week we will learn about file namdling and exception handling.')
    
#count the number of words
word_count = len(text.split())
#convert the text to uppercase
upper_text= text.upper()
#open the output file and write the processed text and word count
with open("weekly chalenge.txt", "w") as file:
    file.write("Processed text:\n")
    file.write(upper_text + "\n")
    file.write(f"word count:{word_count}\n")

    #print success message
print("Done! 'weekly challenge.txt' has been created.")