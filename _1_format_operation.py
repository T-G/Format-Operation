'''
Here are the placeholders and their data types:
%s: string
%d: integer
%f: float %.
nf: float with n decimal places
'''

# %s
day ='Monday'
my_string = 'Today id %s ' %day
print(my_string)

# %d
num = 28
print('%d is a perfect number: ' %num)

# %f
import math

pi = math.pi
text = 'pi number in math: %f '%pi
print(text)

# %.nf
text2 = 'pi number in math: %.2f '%pi
print(text2)


# Multiple placeholder with % operator.passing a tuple (1991, 30)
info = 'Python released in %d and being used for %.1f years'%(1991, 30)
print(info)

# Tuple with % operator
info_tuple = ('Peter', 'Parker', 28)
question = "%s %s is %d years old"%info_tuple
print(question)

# Dictionary with % operator
file = {
    'path' : './com/pty.py',
    'version' : 1.8,
    'author' : 'Musa Arda'
}

file_info = "P: %(path)s\nV: %(version).1f\nA: %(author)s"%file
print('Output from Dictionary')
print(file_info)