# without indexing
hi = 'Hi there! {} {}'
print(hi.format('Peter','Parker'))


# with indexing
statment = "The word {0} has {1} letters"
print(statment.format('Python', len('Python')))


# parameter names
text = '{n} comes from {s}'
language = text.format(n='Python', s='Monty Python\'s Flying Circus')
print(language)


# named placeholders
text1 = '{lang} comes from {source}'
language2 = text1.format(lang='Java', source='Java Coffee type, in Java Island')
print(language2)