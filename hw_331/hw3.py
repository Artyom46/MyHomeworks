word_input = input('Введите слово: ').lower()

if word_input == word_input[::-1]:
    print(f'Слово "{word_input}" является палиндромом!')
else:
    print(f'Слово"{word_input}" не является палиндромом!')
