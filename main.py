primer = "молоко"
nothingvow = 'аоуэ'
softvow = 'и'
jvow = 'еёюя'
vow = 'аоуэиеёюя'
# звонкий + глухой = звонкий
dingcon = ['б', 'в', 'г', 'д', 'ж', 'з']
shhcon = ['п', 'ф', 'к', 'т', 'ш', 'с']
reducts = {'а': ['а', 'а', 'ь'], 'о': ['о', 'а', 'ъ'], 'у': ['у', 'у', 'ъ'], 'э': ['э', 'э', 'ъ'], 'и': ['и', 'и', 'ь'],
           'е': ["`э", '`и', '`ь'], 'ё': ['`о', '`о', '`о'], 'ю': ['`у', '`у', '`ъ'], 'я': ['`а', '`а', '`ь']}


def reduction(word):
    reds = []
    udar = False
    for c in word:
        low = c.lower()
        if low in vow:
            if ord(c) < ord('а'):
                reds.pop()
                reds.append(2)
                reds.append(3)
                reds.append(2)
                udar = True
        elif udar:
            udar = False
        else:
            reds.append(1)


def transcr(word: str, stress: int):
    n = len(word)
    phoword = word
    return f'[{phoword}]'
