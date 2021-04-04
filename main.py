sentence = 'The quick brown fox jumped over the lazy dog.'

query_one = sentence.find('quick') #encuentra la posición, si no existe devuelve un número negativo

query_two = sentence.index('fox') #encuentra la posición, si no existe devuelve error

query_three = 'jumped' in sentence

query_four = 'oops' in sentence


print(query_one)
print(query_two)
print(query_three)
print(query_four)