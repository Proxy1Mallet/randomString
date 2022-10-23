choice = __import__('random').choice

def RandomString(a, abcCase, intCase) -> str:
    for _ in range(int(input('input >>> '))):
        a += choice([str(choice(abcCase)).upper(), str(choice(abcCase)), choice(intCase)])
    return a

print(RandomString(a = '',
                   abcCase = 'abcdefghijklmnopqrstuvwxyz',
                   intCase = '123456789'))