'''Write a Python function to reverses a string if its length is a multiple of 4. '''

def reverse_string(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string
print(reverse_string('code'))
print(reverse_string('python'))
print(reverse_string('ILAMARKA'))