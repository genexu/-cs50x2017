import sys

def main():
    if arg_checker(sys.argv) != True:
        print('Usage: ./caesar k')
        return 1

    kstring = sys.argv[1]
    plaintext = input('plaintext:  ')

    if plaintext == None:
        return 0

    space_count = 0
    print('ciphertext: ', end='');
    for index, s in enumerate(plaintext):
        ascii_s = ord(s)
        if ascii_s == 32:
            space_count += 1
        k = ord(kstring[(index - space_count) % len(kstring)])
        if k > 64 and k < 91:
            k -= 65
        if k > 96 and k < 123:
            k -= 97
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

def arg_checker(argv):
    if len(argv) != 2:
        return False

    kstring = argv[1]
    for s in kstring:
        if ord(s) < 64 or ord(s) > 122:
            return False
        if ord(s) > 90 and ord(s) < 97:
            return False
    return True

if __name__ == '__main__':
    main()