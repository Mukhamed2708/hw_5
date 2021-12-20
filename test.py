import re


class Person:

    def __init__(self, last_name, first_name, email, file, color):
        self.last_name = last_name
        self. first_name = first_name
        self.email = email
        self.file = file
        self.color = color


data = open('MOCK_DATA.txt', 'r')
text = data.read()

last_name = open('last_name.txt', 'w')
first_name = open('first_name.txt', 'w')
full_name = open('full_name.txt', 'w')
emails = open('emails.txt', 'w')
files = open('files.txt', 'w')
colors = open('colors.txt', 'w')

lines = re.split('\n', text)
print(len(lines))
persons = []

for line in lines:
    if line == '':
        continue
    print(line)
    splitted = re.split('\t', line)
    persons.append(Person(splitted[0], splitted[1], splitted[2], splitted[3], splitted[4]))

for person in persons:
    last_name.write(person.last_name + '\n')
    first_name.write(person.first_name + '\n')
    full_name.write(person.first_name + ' ' + person.last_name + '\n')
    emails.write(person.email + '\n')
    files.write(person.file + '\n')
    colors.write(person.color + '\n')

last_name.close()
first_name.close()
full_name.close()
emails.close()
files.close()
colors.close()
data.close()
