#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cs50.h>

bool arg_checker(int c, string v[]);

int main(int argc, string argv[]) {
    if (!arg_checker(argc, argv)) {
        printf("Usage: ./caesar k\n");
        return 1;
    }

    string kstring = argv[1];

    printf("plaintext:  ");
    string s = get_string();

    int space_count = 0;
    if (s != NULL) {
        printf("ciphertext: ");
        for (int i = 0, n = strlen(s); i < n; i++) {
            int ascii_s = (int)s[i];
            if (ascii_s == 32) {
                space_count++;
            }

            int k = (int)kstring[(i - space_count) % strlen(kstring)];

            if (k > 64 && k < 91) {
                k -= 65;
            }
            if (k > 96 && k < 123) {
                k -= 97;
            }
            if (ascii_s > 64 && ascii_s < 91) {
                if ((ascii_s + k) > 90) {
                    printf("%c", ascii_s + k - 26);
                }
                else {
                    printf("%c", ascii_s + k);
                }
            }
            else if (ascii_s > 96 && ascii_s < 123) {
                if ((ascii_s + k) > 122) {
                    printf("%c", ascii_s + k - 26);
                }
                else {
                    printf("%c", ascii_s + k);
                }
            }
            else {
                printf("%c", s[i]);
            }
        }
        printf("\n");
    }
}

bool arg_checker(int c, string v[]) {
    if (c < 2 || c > 2) {
        return false;
    }
    string kstring = v[1];
    for (int i = 0, n = strlen(kstring); i < n; i++) {
        if ((int)kstring[i] < 64 || (int)kstring[i] > 122) {
            return false;
        }
        if ((int)kstring[i] > 90 && (int)kstring[i] < 97) {
            return false;
        }
    }
    return true;
}