from string import Template
name = 'Bruce Wayne'
hero = 'Batman'

# $h and $s are placeholders
# create a Template object
temp = Template('$h is $n')
# call the substitute method on the Template class
# parameter name must be same as the placeholder names
print(temp.substitute(h=hero, n=name))

# Ex: 2
num_1 = 5
num_2 = 8
result = num_1 + num_2

temp2 = Template('$a + $b = $c')
result = temp2.substitute(a=num_1, b=num_2, c=result)
print(result)
