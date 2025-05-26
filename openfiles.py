#open a file in read mode.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('new.txt','w')as file:
    file.write('Hello world wwwwwww, welcome to rasa technologies webinar session')

