#include <stdio.h>
#include <cs50.h>

int main(void) {
    printf("Minutes: ");
    int x = get_int();
    printf("Bottles: %i\n", x * 12);
}