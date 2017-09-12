#include <stdio.h>
#include <cs50.h>

int main(void) {
    int x = -1;
    while(x < 0 || x > 23) {
        printf("Height: ");
        x = get_int();
    }

    for (int i = 0; i < x; i++) {
        for (int j = x - 1 - i; j > 0; j--) {
            printf(" ");
        }
        for (int j = 0; j < 1 + i; j++) {
            printf("#");
        }
        printf("  ");
        for (int j = 0; j < 1 + i; j++) {
            printf("#");
        }
        printf("\n");
    }
}