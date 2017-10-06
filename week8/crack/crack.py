import sys
import itertools
import crypt
def main():
    if len(sys.argv) != 2:
        print('Usage: ./crack hash');
        return 1;

    hashstr = sys.argv[1]
    salt = hashstr[0:2];

    unit = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    for i in range(1,5):
        for indices in itertools.product(unit, repeat=i):
            key = ''.join(indices)
            if crypt_checker(key, salt, hashstr):
                print(key)
                return 0

def crypt_checker(key, salt, hashstr):
    ciphertext = crypt.crypt(key, salt)
    if ciphertext == hashstr:
        return True
    return False

if __name__ == '__main__':
    main()