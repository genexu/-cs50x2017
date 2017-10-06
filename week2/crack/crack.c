#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>

const int MAX_PASSWORD_LENGTH  = 1;

char *get_salt(char* hash);
bool crypt_checker(char *key, char *salt, char *hash);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    char *hash = argv[1];

    char *salt = get_salt(hash);

    char *unit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char buf[5];
    for (int l1 = 0; l1 < 52; l1++) {
        if (crypt_checker(&unit[l1], salt, hash)) {
            printf("%c\n", unit[l1]);
            return 0;
        }
        for (int l2 = 0; l2 < 52; l2++) {
            snprintf(buf, sizeof buf, "%c%c", unit[l1], unit[l2]);
            if (crypt_checker(buf, salt, hash)) {
                printf("%s\n", buf);
                return 0;
            }
            for (int l3 = 0; l3 < 52; l3++) {
                snprintf(buf, sizeof buf, "%c%c%c", unit[l1], unit[l2], unit[l3]);
                if (crypt_checker(buf, salt, hash)) {
                    printf("%s\n", buf);
                    return 0;
                }
                for (int l4 = 0; l4 < 52; l4++) {
                    snprintf(buf, sizeof buf, "%c%c%c%c", unit[l1], unit[l2], unit[l3], unit[l4]);
                    if (crypt_checker(buf, salt, hash)) {
                        printf("%s\n", buf);
                        return 0;
                    }
                }
            }
        }
    }
}

bool crypt_checker(char *key, char *salt, char *hash) {
    char *ciphertext;
    ciphertext = crypt(key, salt);

    if (strcmp(ciphertext, hash) == 0) {
        return true;
    }
    return false;
}

char *get_salt(char* hash) {
    char *salt = (char *) malloc(3);
    salt[0] = hash[0];
    salt[1] = hash[1];
    salt[2] = '\0';
    return salt;
}