choice = __import__('random').choice

def RandomString(a, lang : str, intCase : str) -> str:
    if lang == 'RU': abcCase = 'абвгдеёжзийклмопрстуфхцчъьэюя'
    else: abcCase = 'abcdefghijklmnopqrstuvwzyz'

    for _ in range(int(input('input >>> '))):
        a += choice([str(choice(abcCase)).upper(), str(choice(abcCase)), choice(intCase)])
    return a

print(RandomString(a = '',
                   lang = 'RU',
                   intCase = '123456789'))