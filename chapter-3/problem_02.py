#  Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected!
<|Date|
'''

print(letter.replace('<|Name|>', 'Abu Bokor').replace('<|Date|', '6 October 2024'))