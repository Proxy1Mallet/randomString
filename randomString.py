from random import choices

def RandomString(lang : str, intCase) -> str:
    if lang == 'RU': abcCase = 'абвгдеёжзсийклмнопрстуфхччъьэюя'
    else: abcCase = 'abcdefghijklmnopqrstuvwxyz'

    a = ''.join(choices(f'{abcCase} {intCase}', k=462))
    return a

print(RandomString(lang='RU', intCase='123456789'))