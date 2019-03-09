def vigenere(text, key, decrypt=false):
    shifts = [ord(k) - ord('a') for k in key.lower()]
    i = 0
    def do_shift(char):
        nonlocal i
        if char.isalpha():
            shift = shifts[i] if not decrypt else MODULE - shifts[i]
            i = (i + 1) % len(key)
            return shift_by(char, shift)
        return char
    return ''.join(map(do_shift, text))
