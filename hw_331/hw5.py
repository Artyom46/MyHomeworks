secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
                 ['оafбasdf%^о^FFжа$#af243ю'], ['afпFsfайFтFsfо13н'], ['fн13Fа1234де123юsdсsfь'],
                 ['чFFтF#Fsfsdf$$о'], ['и$ #sfF'], ['вSFSDам'], ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
                 ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]

small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
             'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
             'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
             'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for sector in secret_letter:
    for elements in sector:
        print(' ', end='')
        for letter in elements:
            if letter in small_rus:
                print(letter, end = '')

# Расшифровка
