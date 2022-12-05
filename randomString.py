def RandomString(intCase, abcCase) -> str:
    a = ''.join(__import__('random').choices(f'{abcCase} {intCase}', k=int(input('Number of characters >>> '))))
    return a
print(RandomString(intCase='123456789', abcCase = 'abcdefghijklmnopqrstuvwxyz'))