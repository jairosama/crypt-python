MODULE = len(string.ascii_lowercase) # 26 para el alfabeto ASCII inglés

def shift_by(char, shift):
    if char.isalpha():
        aux = ord(char) + shift
        z = 'z' if char.islower() else 'Z'
        if aux > ord(z):
            aux -= MODULE
        char = chr(aux)
    return char

def caesar(text, key):
    return ''.join(map(lambda char: shift_by(char, key), text))
