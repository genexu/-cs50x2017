#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cs50.h>

int main(int argc, string argv[]) {
    if (argc < 2 || argc > 2) {
        printf("Usage: ./caesar k\n");
        return 1;
    }
    int k = atoi(argv[1]) % 26;
    printf("plaintext:  ");
    string s = get_string();
    if (s != NULL) {
        printf("ciphertext: ");
        for (int i = 0, n = strlen(s); i < n; i++) {
            int ascii_s = (int)s[i];
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