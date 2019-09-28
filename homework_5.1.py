sentence = input('Enter your sentence :')
deleted_symbol = input('Enter your symbol, which you want to delete :')
sentence_2 = []

for symbol in sentence:
    if symbol != deleted_symbol:
        sentence_2.append(symbol)

sentence_2 = ''.join(sentence_2)
print(sentence_2)
