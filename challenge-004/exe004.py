something = input('Type something: ')

print('The primitive data type of this value is ', type(something))

print('Only has spaces? {}'.format(something.isspace()))
print('Is it a number? {}'.format(something.isnumeric()))
print('Is it alphabetical? {}'.format(something.isalpha()))
print('Is it alphanumeric? {}'.format(something.isalnum()))
print('Is it in uppercase? {}'.format(something.isupper()))
print('Is it in lowercase? {}'.format(something.islower()))
print('Is it capitalized? {}'.format(something.istitle()))
