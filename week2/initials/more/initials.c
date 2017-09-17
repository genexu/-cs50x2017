#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

int main(void) {
    string s = get_string();
    if (s != NULL) {
        for (int i = 0, n = strlen(s); i < n; i++) {
            if ((int)s[i] != 32) {
                if (i == 0 || (int)s[i - 1] == 32) {
                    printf("%c", toupper(s[i]));
                }
            }
        }
        printf("\n");
    }
}