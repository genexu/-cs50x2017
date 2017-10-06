import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: ./caesar k')
        return 1
    k = int(sys.argv[1]) % 26

    plaintext = input('plaintext:  ')
    if plaintext == None:
        return 1

    print('ciphertext: ', end='');
    for s in plaintext:
        ascii_s = ord(s)
        if ascii_s > 64 and ascii_s < 91:
            if (ascii_s + k) > 90:
                print(chr(ascii_s + k - 26), end= '');
            else:
                print(chr(ascii_s + k), end= '');
        elif ascii_s > 96 and ascii_s < 123:
            if (ascii_s + k) > 122:
                print(chr(ascii_s + k - 26), end= '');
            else:
                print(chr(ascii_s + k), end = '');
        else:
            print(s, end = '');
    print('')
    return 0

if __name__ == '__main__':
    main()